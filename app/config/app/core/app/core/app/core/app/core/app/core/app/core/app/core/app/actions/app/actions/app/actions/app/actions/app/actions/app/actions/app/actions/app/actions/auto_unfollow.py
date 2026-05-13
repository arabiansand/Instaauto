from app.core.randomizer import smart_sleep


def unfollow_users(client, user_ids):
    for user_id in user_ids:
        client.user_unfollow(user_id)
        smart_sleep()
