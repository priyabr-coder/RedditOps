import streamlit as st
import os

# Set the page config
st.set_page_config(page_title="Reddit Automation Tool", layout="wide", page_icon="🛠️")

# Top sidebar navigation
st.sidebar.title("Reddit Automation Tool")
page = st.sidebar.selectbox(
    "Choose a Feature:",
    ["Welcome"]
)

# Welcome Page
if page == "Welcome":
    st.title("🛠️ Reddit Automation Tool")
    st.markdown("""
    Welcome to the **Reddit Automation Tool**! 👋  

    Use the sidebar to navigate between:

    - 🧾 **Username Scraper** — Extract usernames from subreddit posts  
    - 📩 **Messaging** — Send messages to collected users  
    - 📝 **Post/Comment Automation** — Automate posting, commenting, and more
    """)

# Username Scraper Page
elif page == "Username Scraper":
    st.title("🧾 Username Scraper")

    from reddit_bot.reddit_auth import reddit_instance
    from reddit_bot.fetch_posts import fetch_subreddit_posts
    from reddit_bot.username_scraper import extract_usernames
    from reddit_bot.utils import save_usernames_to_csv

    subreddit_input = st.text_input("Enter Subreddit:", value="learnpython")
    post_type = st.selectbox("Select Post Type", ["hot", "new", "top", "rising"])
    limit = st.slider("Number of Posts", min_value=1, max_value=100, value=10)

    if st.button("Scrape Usernames"):
        with st.spinner("Fetching data..."):
            reddit = reddit_instance()
            posts = fetch_subreddit_posts(reddit, subreddit_input, post_type, limit)
            user_data = extract_usernames(posts)  # returns list of dicts now

            if not user_data:
                st.warning("No messageable users found.")
            else:
                import pandas as pd
                df = pd.DataFrame(user_data)
                os.makedirs("data", exist_ok=True)
                df.to_csv("data/usernames.csv", index=False)

                st.success(f"✅ Scraped {len(df)} messageable usernames.")
                st.dataframe(df)

                with open("data/usernames.csv", "rb") as f:
                    st.download_button("Download CSV", f, file_name="usernames.csv")




