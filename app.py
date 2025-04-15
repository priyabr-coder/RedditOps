import streamlit as st

# Set the page config (optional)
st.set_page_config(page_title="Reddit Automation Tool", layout="wide")

# Sidebar with navigation links
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select a Page:",
    options=["Welcome", "Username Scraper", "Messaging", "Post/Comment Automation"]
)

# Display content based on the selected page
if page == "Welcome":
    st.title("🔧 Reddit Automation Tool")
    st.markdown("""
    Welcome to the Reddit Automation Tool!  
    Use the sidebar to navigate between:
    
    - 🧾 **Username Scraper**: Scrape usernames from a subreddit.
    - 📩 **Messaging**: Send messages to users (coming soon).
    - 📝 **Post/Comment Automation**: Automate posts and comments (coming soon).
    """)
    
elif page == "Username Scraper":
    st.title("🧾 Username Scraper")
    
    # Importing the username scraping functionality
    from reddit_bot.reddit_auth import reddit_instance
    from reddit_bot.fetch_posts import fetch_subreddit_posts
    from reddit_bot.username_scraper import extract_usernames
    from reddit_bot.utils import save_usernames_to_csv
    import os

    # UI to get subreddit, post type, and limit
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
                
elif page == "Messaging":
    st.title("📩 Messaging Tool (Coming Soon)")
    st.info("This feature will allow you to message Reddit users from your collected list.")
    
elif page == "Post/Comment Automation":
    st.title("📝 Post & Comment Automation (Coming Soon)")
    st.info("This feature will allow automated posting, commenting, upvoting, etc.")
