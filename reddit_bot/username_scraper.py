def extract_usernames(posts):
    usernames = set()
    for post in posts:
        if post.author:
            usernames.add(post.author.name)
        post.comments.replace_more(limit=0)
        for comment in post.comments:
            if comment.author:
                usernames.add(comment.author.name)
    return list(usernames)
