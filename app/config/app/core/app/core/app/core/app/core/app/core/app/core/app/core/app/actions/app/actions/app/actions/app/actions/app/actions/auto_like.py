from app.core.randomizer import smart_sleep


def like_media(client, media_ids):
    for media_id in media_ids:
        client.media_like(media_id)
        smart_sleep()
