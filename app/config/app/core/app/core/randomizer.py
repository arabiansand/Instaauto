import random
import time


def smart_sleep(min_seconds=10, max_seconds=30):
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)
