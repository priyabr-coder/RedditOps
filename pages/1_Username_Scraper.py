import streamlit as st
from reddit_bot.reddit_auth import reddit_instance
from reddit_bot.fetch_posts import fetch_subreddit_posts
from reddit_bot.username_scraper import extract_usernames
from reddit_bot.utils import save_usernames_to_csv
import os

st.title("🧾 Username Scraper")

subreddit_input = st.text_input("Enter Subreddit:", value="learnpython")
post_type = st.selectbox("Select Post Type", ["hot", "new", "top", "rising"])
limit = st.slider("Number of Posts", min_value=1, max_value=100, value=10)

if st.button("Scrape Usernames"):
    with st.spinner("Fetching data..."):
        reddit = reddit_instance()
        posts = fetch_subreddit_posts(reddit, subreddit_input, post_type, limit)
        usernames = extract_usernames(posts)
        os.makedirs("data", exist_ok=True)
        save_usernames_to_csv(usernames)
        st.success(f"Scraped {len(usernames)} unique usernames.")
        st.dataframe(usernames)
        with open("data/usernames.csv", "rb") as f:
            st.download_button("Download CSV", f, file_name="usernames.csv")
