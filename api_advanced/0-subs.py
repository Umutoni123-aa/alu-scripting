#!/usr/bin/python3
"""
Returns the number of subscribers from a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """ Set a custom header user-agent """
    headers = {"User-Agent": "ALU-scripting API 0.1"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    try:
        response = requests.get(url, allow_redirects=False)
    except requests.exceptions.RequestException:
        return 0

    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    else:
        return 0
