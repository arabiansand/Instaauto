import json


def scrape_followers(client, username):
    user_id = client.user_id_from_username(username)
    followers = client.user_followers(user_id)

    data = [
        {
            "username": u.username,
            "full_name": u.full_name
        }
        for u in followers.values()
    ]

    with open(f"data/exports/{username}_followers.json", "w") as f:
        json.dump(data, f, indent=2)
