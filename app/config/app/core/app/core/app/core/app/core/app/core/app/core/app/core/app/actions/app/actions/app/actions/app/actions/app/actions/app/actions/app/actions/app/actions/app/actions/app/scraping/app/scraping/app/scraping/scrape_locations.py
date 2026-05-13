import json


def scrape_location(client, location_id):
    medias = client.location_medias_recent(location_id, amount=20)

    with open(f"data/exports/location_{location_id}.json", "w") as f:
        json.dump([m.dict() for m in medias], f, indent=2)
