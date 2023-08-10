#!/usr/bin/python3
"""
Script that returns the numbers of top 10 hot 
post listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """Function that returns the numbers of
    subscribers of a subreddit passed to it"""

    header = {"User-Agent" : "Mozilla/5.0"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    query_string = {"limit" : 10}

    get_api = requst.get(url, headers=header, allow_redirects=False)

    if get_api.status.code == 200:
        data = get_api.json()
        top_hots = data.get("data").get("children")
        for hot_topics in top_hots:
            top = hot_topics.get("data").get("title")
            print(top)
    else:
        print(None)
    return 0
