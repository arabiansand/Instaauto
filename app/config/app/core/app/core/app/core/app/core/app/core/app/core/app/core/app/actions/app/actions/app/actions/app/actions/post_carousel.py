from pathlib import Path


def post_carousel(client, media_paths, caption=""):
    media = [Path(p) for p in media_paths]

    return client.album_upload(
        paths=[str(m) for m in media],
        caption=caption
    )
