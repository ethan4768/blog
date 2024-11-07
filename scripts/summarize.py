import logging

from utils import call_openai

SUMMARY_SYSTEM_PROMPT = """You are an AI-powered assistant to help people understand the content more easily. 
In your responses, obey the following rules:
- All response have to be markdown-formatted.
- Don't explain or repeat yourself.
- Read the full text to make sure you don't lose important information when answering questions.

总结下面的文章，给出总结、摘要、观点三个部分内容，其中观点部分要使用列表列出，用简体中文以 markdown 格式回复
"""


def summarize_content(raw_content: str) -> str | None:
    try:
        return call_openai(SUMMARY_SYSTEM_PROMPT, raw_content)
    except Exception as e:
        logging.error(e)
        return None
