import argparse
import json
import logging
import os
from datetime import datetime
from pathlib import Path

import httpx
from dotenv import load_dotenv

from model import Post
from retrieve import retrieve_raw_content
from summarize import summarize_content
from utils import push_to_bark

ignore_domains = os.environ.get("IGNORE_URLS", "x.com,twitter.com")
ignore_domain_list = [domain.strip() for domain in ignore_domains.split(',')]


def get_post_info_from_commit():
    latest_commit_message = os.environ["LATEST_COMMIT_MESSAGE"]
    if not latest_commit_message:
        return None

    commit_body = latest_commit_message.split("\n\n")[1].strip()
    data = json.loads(commit_body)
    data['timestamp'] = datetime.strptime(data['timestamp'], "%Y-%m-%dT%H:%M:%S%z")

    return Post(**data)


def ignore_url(url: str) -> bool:
    try:
        parsed_url = httpx.URL(url)
        return any(parsed_url.host == domain or parsed_url.host.endswith('.' + domain) for domain in ignore_domain_list)
    except Exception as e:
        logging.error(e)
        return False


def get_content_file_path(post: Post, file_type: str) -> Path:
    """
    :param post: post
    :param file_type: raw/summary
    """
    filename = f'{post.slug}.md'
    return Path("src", "content", "bookmarks", file_type, filename)


def with_metadata(file_type: str, post: Post, content: str) -> str:
    return f"""---
title: {post.title}
description: {post.description}
pubDatetime: {post.timestamp.isoformat()}
ogImage: {post.image}
tags: 
  - {file_type}
---

[原文链接]({post.url}) | [原文内容](../raw/{post.slug}) | [AI 总结](../summary/{post.slug})

---

{content}
"""


def write_content(path: Path, content: str) -> bool:
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf8') as f:
            f.write(content)
        return True
    except Exception as e:
        logging.error(e)
        return False


def push_notification(post: Post, process_error_msg: str):
    is_successful = True if not process_error_msg else False
    process_result = "SUCCESS" if is_successful else "FAILURE"
    msg = f"""
[GITHUB ACTION POST PROCESS]: {process_result} 
{f"ERROR MESSAGE: {process_error_msg}" if not is_successful else ""} 
- url: {post.url}
- title: {post.title}
- tags: {".".join(post.tags)}
- description: {post.description}
- timestamp: {post.timestamp.isoformat()}  
"""
    push_success_result = os.environ.get("PUSH_SUCCESS_RESULT", "false").lower() in ('true', '1', 't', 'on')
    if not is_successful or push_success_result:
        push_to_bark(msg, "github-automatic-summarization")


def process(post: Post) -> str:
    # raw content
    raw_file_path = get_content_file_path(post, "raw")
    raw_content = retrieve_raw_content(post.url)
    if not raw_content:
        return "[retrieve] Cannot retrieve raw content"
    raw_content_with_metadata = with_metadata("raw", post, raw_content)
    write_raw_content_result = write_content(raw_file_path, raw_content_with_metadata)
    if not write_raw_content_result:
        return f"[retrieve] Cannot write to file {str(raw_file_path)}"
    logging.info(f"[retrieve] write successfully to {str(raw_file_path)}")

    # summary
    summary_file_path = get_content_file_path(post, "summary")
    summary_content = summarize_content(raw_content)
    if not summary_content:
        return "[summarize] Cannot summarize content"
    summary_content_with_metadata = with_metadata("summary", post, summary_content)
    write_summary_content_result = write_content(summary_file_path, summary_content_with_metadata)
    if not write_summary_content_result:
        return f"[summarize] Cannot write to {str(summary_file_path)}"

    logging.info(f"[summarize] write successfully to {str(summary_file_path)}")
    return ""


def main():
    post = get_post_info_from_commit()
    if not post:
        return "No post found"

    # ignore some urls, e.g., x.com, twitter.com
    if ignore_url(post.url):
        return "url ignored"

    result = process(post)
    push_notification(post, result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Enable test mode, will load env file')
    args = parser.parse_args()

    if args.test:
        load_dotenv(verbose=True)

    m = main()
    print(m)
