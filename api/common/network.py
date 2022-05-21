import os
import re
import requests

API_HOST = os.getenv("API_HOST", "http://localhost:1337")


def is_up(url: str, title: str) -> bool:
    try:
        src_code = str(requests.get(url).content)
        if re.search(f"<title>{title}", src_code):
            return True
        return False
    except requests.exceptions.ConnectionError:
        # Couldn't resolve connection
        return False


def api_get(endpoint: str, method="GET", timeout=None, **params) -> requests.request:
    headers = {}
    headers["User-Agent"] = "rere-util"
    return requests.request(method, f"{API_HOST}/{endpoint}", timeout=timeout, headers=headers, params=params)


if __name__ == "__main__":
    ret = api_get("api/info", timeout=2)
    print(ret, ret.text)
