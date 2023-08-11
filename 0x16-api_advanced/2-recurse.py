#!/usr/bin/python3
"""Recurse the list"""

import requests


def recurse(subreddit, hot_list=[], nxt_link=None):
    """
    Returns a list containing the titles of all hot articles for a given
    subreddit. If no results are found for the given subreddit, the function
    should return None.
    """
    headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    query_string = {"limit": 10, "after": nxt_link}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        data = res.json
        nxt_link = data.get("data").get("after")
        levels = data.get("data").get("children")
        for hot_topics in levels:
            top = hot_topics.get("data").get("title")
            hot_list.append(top)
            print(top)
        print(nxt_link)
        if nxt_link is not None:
            recurse(subreddit, hot_list, nxt_link)
        return hot_list
    else:
        print(None)
    return 0
