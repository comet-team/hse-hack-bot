import requests
import os


YDISK_URL = "https://cloud-api.yandex.net/v1/disk/resources"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f'OAuth {os.environ["YDISK_OAUTH"]}',
}


def upload(path, file_url):
    params = {"path": path, "url": file_url}
    print(params)
    resp = requests.post(f"{YDISK_URL}/upload", params=params, headers=headers)
    print(resp)
