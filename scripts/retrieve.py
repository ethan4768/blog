import logging

import httpx

from utils import log_execution_time


@log_execution_time
def retrieve_raw_content(url: str) -> str | None:
    timeout = httpx.Timeout(
        connect=5.0,  # 连接超时
        read=20.0,  # 读取超时
        write=10.0,  # 写入超时
        pool=5.0  # 连接池超时
    )

    try:
        with httpx.Client(timeout=timeout) as client:
            response = client.get(
                f"https://r.jina.ai/{url}",
                headers={
                    "Accept": "application/json",
                    # "Authorization": f"Bearer {}",
                },
            )
            result = response.json()
            if result.get('code') == 200:
                return result.get('data', {}).get('content')
            return None
    except Exception as e:
        logging.error(e)
        return None
