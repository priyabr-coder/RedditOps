
import time
import logging
from praw.models import Redditor

def send_messages(reddit, usernames, subject, body, delay=10):
    results = []
    for i, username in enumerate(usernames):
        try:
            user = Redditor(reddit, name=username)
            user.message(subject, body)
            results.append({"username": username, "status": "Sent"})
            logging.info(f"✅ Message sent to {username}")
        except Exception as e:
            results.append({"username": username, "status": f"Failed - {e}"})
            logging.error(f"❌ Failed to message {username}: {e}")
        if i < len(usernames) - 1:
            time.sleep(delay)
    return results
