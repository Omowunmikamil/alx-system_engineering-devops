#!/usr/bin/python3
"""Script that returns the numbers of
subscribers of a subreddit passed to it"""

import requests


def number_of_subscribers(subreddit):
    """Function that returns the numbers of
    subscribers of a subreddit passed to it"""

    headers = {"User-Agent" : "mozilla/5.0"}
    api_url = "https://www.redit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        return response.json().get("data").get("subscribers")
    return (0)
