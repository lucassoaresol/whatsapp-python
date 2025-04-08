from requests import Session
from .config import HOST


class Whatsapp:
    def __init__(self):
        self.session = Session()
        self.URL_BASE_API_CLIENT = HOST
        self.URL_BASE_CHAT = f"{self.URL_BASE_API_CLIENT}/chats"
        self.URL_BASE_MSG = f"{self.URL_BASE_API_CLIENT}/messages"

    def send_msg(self, number, message, message_id=None, mentions=None):
        data = {
            "number": number,
            "message": message,
        }
        if message_id:
            data["message_id"] = message_id
        if mentions:
            data["mentions"] = mentions
        response = self.session.post(
            self.URL_BASE_MSG,
            json=data,
        )
        return response.json()

    def send_msg_contact(self, number, contact_id):
        url = f"{self.URL_BASE_MSG}/{number}/contact/{contact_id}"

        response = self.session.post(url)
        return response.json()

    def get_msg(self, params=None):
        response = self.session.get(self.URL_BASE_MSG, params=params)
        return response.json()

    def retrive_msg(self, id):
        url = f"{self.URL_BASE_MSG}/{id}"
        response = self.session.get(url)
        return response.json()

    def patch_msg(self, id, icon):
        url = f"{self.URL_BASE_MSG}/{id}"
        response = self.session.patch(url, json={"icon": icon})
        return response.json()

    def delete_msg(self, id):
        url = f"{self.URL_BASE_MSG}/{id}"
        response = self.session.delete(url)
        return response.json()

    def get_chat(self):
        response = self.session.get(self.URL_BASE_CHAT)
        return response.json()

    def retrive_chat(self, id):
        url = f"{self.URL_BASE_CHAT}/{id}"
        response = self.session.get(url)
        return response.json()

    def retrive_contact(self, id):
        url = f"{self.URL_BASE_API_CLIENT}/contacts/{id}"
        response = self.session.get(url)
        return response.json()
