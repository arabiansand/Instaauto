import json


def scrape_hashtag(client, hashtag):
    medias = client.hashtag_medias_recent(hashtag, amount=20)

    data = [
        {
            "id": media.id,
            "caption": media.caption_text
        }
        for media in medias
    ]

    with open(f"data/exports/{hashtag}.json", "w") as f:
        json.dump(data, f, indent=2)
