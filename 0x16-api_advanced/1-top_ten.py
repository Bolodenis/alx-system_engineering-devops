#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""
import requests

def top_ten(subreddit):
    try:
        # Base URL for Reddit API
        base_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        headers = {'User-Agent': 'Mozilla/5.0'}

        # Make the request
        response = requests.get(base_url, headers=headers, allow_redirects=False)

        # If the subreddit is invalid or returns a redirect
        if response.status_code == 404:
            print(None)
            return
        
        # Parsing the JSON response
        data = response.json()
        posts = data['data']['children']
        
        # Print the titles of the top 10 hot posts
        for post in posts:
            print(post['data']['title'])
    
    except requests.exceptions.RequestException as e:
          print(None)
