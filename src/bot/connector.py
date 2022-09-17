import random


class Connector:
    def get_chat_id(self):
        return -1001762730288

    def get_chat_name(self):
        return random.choice(["Lorem", "ipsum", "dolor", "sit", "amet"])

    def get_chat_members(self):
        return self.get_chat_id, ["1064231416"]

    def get_admin(self):
        return "750120380"
        # return '1064231416'
