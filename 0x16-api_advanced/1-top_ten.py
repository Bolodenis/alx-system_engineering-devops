#!/usr/bin/python3

'''This module contains the function top_ten.'''

import requests


def top_ten(subreddit):
    '''Gets the top ten topics of a subreddit.'''
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "GetHotTopics/1.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the subreddit exists
        if response.status_code != 200:
            print(None)
            return
        # Parse the JSON response
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        # Print titles of the first 10 hot posts
        if not posts:
            print(None)
        else:
            for post in posts:
                print(post['data']['title'])
    except Exception:
        print(None)
