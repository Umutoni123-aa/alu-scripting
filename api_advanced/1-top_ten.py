#!/usr/bin/python3
"""
1-top_ten.py

Query the Reddit API and print the titles of the first 10 hot posts
for a given subreddit.


"""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU:api_advanced:1.0 (by /u/yourusername)"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
    except Exception:
        print(None)
        return

    if response.status_code != 200:
        print(None)
        return

    try:
        children = response.json().get("data", {}).get("children", [])
    except Exception:
        print(None)
        return

    if not children:
        print(None)
        return

    for child in children:
        title = child.get("data", {}).get("title")
        print(title)
