from pathlib import Path


def post_story(client, media_path):
    media_path = Path(media_path)

    if media_path.suffix.lower() in [".jpg", ".jpeg", ".png"]:
        return client.photo_upload_to_story(str(media_path))

    return client.video_upload_to_story(str(media_path))
