from faker import Faker

fake = Faker()


def random_device_profile():
    return {
        "user_agent": fake.user_agent(),
        "timezone": fake.timezone(),
        "locale": fake.locale()
    }
