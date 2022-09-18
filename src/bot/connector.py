import requests

NOTIFIER_URL = "https://cf5a-89-175-18-189.eu.ngrok.io"
subscribed_groups = set()


def subscribe_to_notifications(chat_id, group_name):
    params = {"chat_id": chat_id, "group_name": group_name}
    print(chat_id)
    if group_name not in subscribed_groups:
        resp = requests.get(f"{NOTIFIER_URL}/", params=params)
        print(resp)
        if resp.status_code == 200:
            subscribed_groups.add(group_name)
