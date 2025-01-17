#!/usr/bin/python3

'''Thismodulecontainsthefunctiontop_ten'''
importjson
importrequests

deftop_ten(subreddit):
'''Getsthetoptentopicsofasubreddit'''
url=f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
headers={"User-Agent":"GetHotTopics/1.0"}

try:
response=requests.get(url,headers=headers,allow_redirects=False)

#Checkifthesubredditexists
ifresponse.status_code!=200:
print(None)
return

#ParsetheJSONresponse
data=response.json()
posts=data.get('data',{}).get('children',[])

#Printtitlesofthefirst10hotposts
ifnotposts:
print(None)
else:
forpostinposts:
print(post['data']['title'])
exceptExceptionase:
print(None)

