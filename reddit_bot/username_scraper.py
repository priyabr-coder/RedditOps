import time
from typing import List, Dict

def is_user_messageable(reddit, username: str) -> bool:
    try:
        redditor = reddit.redditor(username)
        _ = redditor.id  # Triggers API request
        return True
    except Exception:
        return False

def extract_usernames(posts) -> List[Dict]:
    usernames = set()

    for post in posts:
        if post.author and post.author.name:
            usernames.add(post.author.name)

        post.comments.replace_more(limit=0)
        for comment in post.comments:
            if comment.author and comment.author.name:
                usernames.add(comment.author.name)

    print(f"Found {len(usernames)} raw usernames. Checking messageability...")

    messageable_users = []

    for username in usernames:
        try:
            time.sleep(1)  # Respect Reddit rate limits
            if is_user_messageable(post._reddit, username):
                user_data = {
                    "username": username,
                    "messageable": True
                }
                messageable_users.append(user_data)
        except Exception:
            continue  # Ignore broken or inaccessible users

    return messageable_users
