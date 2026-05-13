from app.actions.auto_like import like_media
from app.actions.auto_comment import comment_media


def engage(client, media_ids):
    like_media(client, media_ids)
    comment_media(client, media_ids)
