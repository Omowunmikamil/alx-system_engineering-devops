#!/usr/bin/python3
"""
Script that returns the numbers of top 10 hoit
post listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Function that returns the numbers of
    subscribers of a subreddit passed to it"""

    headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    get_api = requsts.get(url, headers=headers, allow_redirects=False)

    if get_api.status_code == 200:
        data = get_api.json()
        top_hots = data.get("data").get("children")
        for hot_topics in top_hots:
            top = hot_topics.get("data").get("title")
            print(top)
    else:
        print(None)
    return 0
