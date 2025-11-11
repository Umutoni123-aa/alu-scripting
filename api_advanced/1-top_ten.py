#!/usr/bin/python3
"""
Query the Reddit API and print the titles of the first 10 hot posts
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit."""
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "ALUProject:RedditAPI:v1.0 (by /u/StudentExample)",
        "Accept": "application/json",
    }
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Reddit returns 302 for invalid subreddits, and 429 for rate limit
    if response.status_code != 200:
        print(None)
        return

    results = response.json().get("data", {}).get("children", [])

    if not results:
        print(None)
        return

    for post in results:
        title = post.get("data", {}).get("title")
        if title:
            print(title)
