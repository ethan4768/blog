import logging
import os
import re
import time
import uuid
from functools import wraps

import httpx

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Entering {func.__name__}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(
            f"Exiting {func.__name__} - Elapsed time: {elapsed_time:.4f} seconds"
        )
        return result

    return wrapper


def set_output(name, value):
    with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
        print(f"{name}={value}", file=fh)


def set_multiline_output(name, value):
    with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
        delimiter = uuid.uuid1()
        print(f"{name}<<{delimiter}", file=fh)
        print(value, file=fh)
        print(delimiter, file=fh)


def slugify(text: str) -> str:
    # replace invalid fs chars with -
    invalid_fs_chars: str = '/\\:*?"<>|'
    return re.sub(
        r"[" + re.escape(invalid_fs_chars) + r"\s]+", "-", text.lower()
    ).strip("-")


@log_execution_time
def call_openai(prompt: str, content: str) -> str | None:
    api_key = os.environ['OPENAI_API_KEY']
    model: str = os.environ.get('OPENAI_MODEL', 'gpt-4o-mini')
    base_url: str = os.environ.get('OPENAI_BASE_URL', 'https://api.openai.com/v1')
    api_endpoint: str = f'{base_url}/chat/completions'

    headers: dict = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data: dict = {
        "model": model,
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": content}
        ]
    }

    timeout = httpx.Timeout(
        connect=10.0,  # 连接超时
        read=30.0,  # 读取超时
        write=10.0,  # 写入超时
        pool=10.0  # 连接池超时
    )

    with httpx.Client(timeout=timeout) as client:
        response = client.post(
            api_endpoint,
            headers=headers,
            json=data
        )
        if response.status_code != 200:
            return None
        return response.json()['choices'][0]['message']['content']


def push_to_bark(msg: str, group: str):
    device_key = os.environ['BARK_DEVICE_KEY']
    if not device_key:
        return None
    url = f"https://api.day.app/{device_key}"
    headers = {
        'Content-Type': 'application/json; charset=utf-8'
    }
    data = {
        "body": msg,
        "group": group
    }

    return httpx.post(url, headers=headers, json=data)
