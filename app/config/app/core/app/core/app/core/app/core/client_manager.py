from instagrapi import Client
from app.core.logger import logger


class InstagramClientManager:
    def __init__(self, username, password, proxy=None):
        self.username = username
        self.password = password
        self.proxy = proxy
        self.client = Client()

    def login(self):
        if self.proxy:
            self.client.set_proxy(self.proxy)

        self.client.delay_range = [1, 3]

        try:
            self.client.login(self.username, self.password)
            logger.info(f"Logged in: {self.username}")

        except Exception as e:
            logger.error(str(e))
            raise

        return self.client
