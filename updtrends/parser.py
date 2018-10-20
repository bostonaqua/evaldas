import feedparser
from datetime import datetime, timedelta
from django.utils.timezone import make_aware
# title, link, pubDate(published)
FORMAT = '%a, %d %b %Y %H:%M:%S %Z'


# parsing rss by url
def parse(*args):
    url = args[0]
    cat = args[1]
    return (feedparser.parse(url), cat)


# return list with post objects
def get_news(*parsed):
    category = parsed[1]
    posts = []
    feed = parsed[0]['entries']
    for item in feed:
        try:
            desc = item['summary_detail']['value'].lower()
            if item['published'][-3:] == 'EST':
                publ = datetime.strptime(item['published'][:-4], FORMAT[:-3])
                publ = publ + timedelta(hours=4)
            else:
                publ = datetime.strptime(item['published'], FORMAT)
        except (KeyError, ValueError):
            continue
        posts.append({
            'title': item['title'],
            'link': item['link'],
            'pubdate': make_aware(publ),
            'description': desc,
            'category': category,
        })
    return posts


# return list of trend words
def get_trends(*parsed):
    country = parsed[1]
    trends = []
    trendlist = parsed[0]['entries']
    for item in trendlist:
        trends.append({
            'trend': item['title'],
            'country': country,
        })
    return trends
