import streamlit as st
import praw
import pandas as pd
from dotenv import load_dotenv
import os

# Load credentials from .env file
load_dotenv()

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# Initialize Reddit API
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD,
    user_agent=REDDIT_USER_AGENT
)

# Streamlit App
st.title("Reddit Username Collector")

subreddit_input = st.text_input("Enter Subreddit Name", value="learnpython")
fetch_btn = st.button("Fetch Usernames")

if fetch_btn and subreddit_input:
    with st.spinner("Fetching usernames..."):
        subreddit = reddit.subreddit(subreddit_input)
        usernames = set()

        for post in subreddit.new(limit=100):  # 100 posts to increase chances of unique 50
            if post.author:
                usernames.add(str(post.author))
            if len(usernames) >= 50:
                break

        usernames_list = list(usernames)
        df = pd.DataFrame(usernames_list, columns=["Username"])

        # Display in Streamlit
        st.success(f"Fetched {len(usernames_list)} unique usernames from r/{subreddit_input}")
        st.dataframe(df)

        # Save to CSV
        csv_file = f"usernames_{subreddit_input}.csv"
        df.to_csv(csv_file, index=False)
        st.download_button("Download CSV", data=df.to_csv(index=False), file_name=csv_file, mime="text/csv")
