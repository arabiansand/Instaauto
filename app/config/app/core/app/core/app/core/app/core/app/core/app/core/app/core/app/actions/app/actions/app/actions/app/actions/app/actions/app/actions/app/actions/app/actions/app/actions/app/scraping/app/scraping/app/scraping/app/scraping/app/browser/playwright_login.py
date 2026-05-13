from playwright.sync_api import sync_playwright
import time
import random


class BrowserLogin:
    def __init__(self, headless=True):
        self.headless = headless

    def login(self, username, password):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.headless)
            page = browser.new_page()

            page.goto("https://www.instagram.com/accounts/login/")

            time.sleep(random.uniform(3, 6))

            page.fill('input[name="username"]', username)
            time.sleep(random.uniform(1, 2))

            page.fill('input[name="password"]', password)
            time.sleep(random.uniform(1, 2))

            page.click('button[type="submit"]')

            time.sleep(10)

            browser.close()
