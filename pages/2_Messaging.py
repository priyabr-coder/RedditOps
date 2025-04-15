# pages/2_Messaging.py

import streamlit as st
import pandas as pd
from reddit_bot.reddit_auth import reddit_instance
from reddit_bot.messenger import send_messages

st.title("📩 Reddit Messaging Tool")

# Load usernames
try:
    df = pd.read_csv("data/usernames.csv")
    usernames = df['username'].dropna().unique().tolist()
    if not usernames:
        st.warning("No usernames found. Please scrape users first.")
except FileNotFoundError:
    usernames = []
    st.warning("usernames.csv not found. Please scrape usernames first.")

if usernames:
    st.markdown("### ✅ Select Users to Message")
    selected_users = st.multiselect("Usernames", usernames, default=usernames[:10])

    st.markdown("### 📝 Compose Your Message")
    subject = st.text_input("Subject")
    body = st.text_area("Message Body", height=200)

    delay = st.slider("⏱️ Delay between messages (in seconds)", 5, 60, 10)

    if st.button("Send Messages"):
        if not subject or not body:
            st.warning("Please fill in both subject and message body.")
        elif not selected_users:
            st.warning("Please select at least one user.")
        else:
            with st.spinner("Sending messages..."):
                reddit = reddit_instance()
                result = send_messages(reddit, selected_users, subject, body, delay)
                result_df = pd.DataFrame(result)
                st.success("✅ Messaging complete.")
                st.dataframe(result_df)
