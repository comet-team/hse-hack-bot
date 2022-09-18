import requests

NOTIFIER_URL = "http:/localhost:5000"
subscribed_groups = set()


def subscribe_to_notifications(group_name):
    params = {"group_name": group_name}
    if group_name not in subscribed_groups:
        resp = requests.get(f"{NOTIFIER_URL}/group_name", params=params)
        if resp.status_code == 200:
            subscribed_groups.add(group_name)
