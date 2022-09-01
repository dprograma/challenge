import requests
import json
from .models import DemoNewsModel
from datetime import datetime


def job():
    # external endpoint that returns list of ids
    NEWS_URL = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'

    headers = {'user-agent': 'quickcheck/0.0.1'}
    response = requests.get(NEWS_URL, headers=headers)

    # in order to trim the last element
    result = response.text.split(',')[1:len(response.text.split(','))-2]
    # got this from API " 499287535 ] /n" --> reshaped to that below
    last = response.text.split(',')[-1]
    result.insert(len(result), last.strip().split()[0])  # "499287535"

    news = 400  # 100 downward/latest
    res = [int(id.strip())
            for id in result[news+1:news+6]]  # list comprehension
    
    resp = []
    for id in res:
        NEWS_URL = f'https://hacker-news.firebaseio.com/v0/item/{str(id)}.json?print=pretty'
        headers = {'user-agent': 'quickcheck/0.0.1'}
        response = requests.get(NEWS_URL, headers=headers)
        data = json.loads(response.text)
        resp.append(data)

    # print("RESPONSE: ", resp)

    for r in resp:
        # print("I am here!!!")
        if 'text' not in r:
            text = ''
        else:
            text = r['text']
        if 'url' not in r:
            url = ''
        else:
            url = r['url']
        if 'kids' not in r:
            relatedids = ''
        else:
            relatedids = str(r['kids'])
        name = r['by']
        descendants = r['descendants']
        newsid = r['id']
        score = r['score']
        time = datetime.fromtimestamp(r['time'])
        title = r['title']
        dtype = r['type']

        news_res = DemoNewsModel(newsid=newsid, name=name, relatedids=relatedids, score=score, title=title, newstype=dtype, descendants=descendants, text=text, url=url, created_at=time)
        news_res.save()
