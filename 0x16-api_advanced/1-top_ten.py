#!/usr/bin/python3

'''Thismodulecontainsthefunctiontop_ten'''
import json
import requests

deftop_ten(subreddit):
'''Getsthetoptentopicsofasubreddit'''
url=f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
headers={"User-Agent":"GetHotTopics/1.0"}

try:
    response=requests.get(url,headers=headers,allow_redirects=False)

#Checkifthesubredditexists
    if response.status_code!=200:
        print(None)
        return

#ParsetheJSONresponse
    data=response.json()
    posts=data.get('data',{}).get('children',[])

#Printtitlesofthefirst10hotposts
    if not posts:
        print(None)
    else:
        for post in posts:
            print(post['data']['title'])
except Exception as e:
print(None)

