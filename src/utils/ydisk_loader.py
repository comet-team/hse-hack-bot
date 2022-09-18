import requests
import os


YDISK_URL = "https://cloud-api.yandex.net/v1/disk/resources"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f'OAuth {os.environ["YDISK_OAUTH"]}',
}
ROOT = 'HSE Hack Comet'


def create_dir(path):
    params = {"path": f"{ROOT}/{path}"}
    requests.put(f"{YDISK_URL}", params=params, headers=headers)


def upload(path, file_url):
    params = {"path": f"{ROOT}/{path}", "url": file_url}
    requests.post(f"{YDISK_URL}/upload", params=params, headers=headers)
