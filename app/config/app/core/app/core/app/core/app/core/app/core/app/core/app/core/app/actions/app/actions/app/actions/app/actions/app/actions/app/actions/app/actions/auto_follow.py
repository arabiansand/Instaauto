from app.core.randomizer import smart_sleep


def follow_users(client, user_ids):
    for user_id in user_ids:
        client.user_follow(user_id)
        smart_sleep()
