from app.scraping.scrape_followers import scrape_followers


def scrape_competitors(client, usernames):
    for username in usernames:
        scrape_followers(client, username)
