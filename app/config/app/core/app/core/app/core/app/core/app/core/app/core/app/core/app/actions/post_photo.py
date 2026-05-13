from pathlib import Path


def post_photo(client, image_path, caption=""):
    image_path = Path(image_path)

    if not image_path.exists():
        raise FileNotFoundError(image_path)

    return client.photo_upload(
        path=str(image_path),
        caption=caption
    )
