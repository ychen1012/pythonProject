import json

import requests
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/billboard'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
response = requests.get(url=url, headers=headers)
content = response.text
beautifulsoup = BeautifulSoup(content, 'html.parser')
jsondict = json.loads(beautifulsoup.select("#js-initialData")[0].text)
hostlist = jsondict['initialState']['topstory']['hotList']

for hot in hostlist:
    print(hot['cardId'] + "\n")
    print(hot['target']['titleArea']['text'] + "\n")
    print(hot['target']['excerptArea']['text'] + "\n")
    print(hot['target']['metricsArea']['text'] + "\n")
    print('--------------------------------------------------------------')
