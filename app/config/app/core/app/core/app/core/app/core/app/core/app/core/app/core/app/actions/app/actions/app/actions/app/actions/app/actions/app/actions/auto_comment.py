import random
from app.core.randomizer import smart_sleep

COMMENTS = [
    "Amazing content 🔥",
    "Love this 🙌",
    "Great post 🚀",
    "Very inspiring ✨"
]


def comment_media(client, media_ids):
    for media_id in media_ids:
        client.media_comment(media_id, random.choice(COMMENTS))
        smart_sleep()
