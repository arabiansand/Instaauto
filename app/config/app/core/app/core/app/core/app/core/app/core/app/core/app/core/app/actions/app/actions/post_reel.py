from pathlib import Path


def post_reel(client, video_path, caption=""):
    video_path = Path(video_path)

    return client.clip_upload(
        path=str(video_path),
        caption=caption
    )
