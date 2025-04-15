def fetch_subreddit_posts(reddit, subreddit_name, post_type="hot", limit=10):
    subreddit = reddit.subreddit(subreddit_name)
    if post_type == "new":
        return subreddit.new(limit=limit)
    elif post_type == "top":
        return subreddit.top(limit=limit)
    elif post_type == "rising":
        return subreddit.rising(limit=limit)
    return subreddit.hot(limit=limit)
