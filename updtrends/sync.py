from updtrends import parser
from updtrends.models import Post, Trend


CNN = [
    ('http://rss.cnn.com/rss/edition.rss', 'Top Stories'),
    ('http://rss.cnn.com/rss/edition_world.rss', 'World'),
    ('http://rss.cnn.com/rss/edition_africa.rss', 'Africa'),
    ('http://rss.cnn.com/rss/edition_americas.rss', 'Americas'),
    ('http://rss.cnn.com/rss/edition_asia.rss', 'Asia'),
    ('http://rss.cnn.com/rss/edition_europe.rss', 'Europe'),
    ('http://rss.cnn.com/rss/edition_meast.rss', 'Middle East'),
    ('http://rss.cnn.com/rss/edition_us.rss', 'U.S.'),
    ('http://rss.cnn.com/rss/money_news_international.rss', 'Money'),
    ('http://rss.cnn.com/rss/edition_technology.rss', 'Technology'),
    ('http://rss.cnn.com/rss/edition_space.rss', 'Science & Space'),
    ('http://rss.cnn.com/rss/edition_entertainment.rss', 'Entertainment'),
    ('http://rss.cnn.com/rss/edition_sport.rss', 'World Sport'),
    ('http://rss.cnn.com/rss/edition_football.rss', 'Football'),
    ('http://rss.cnn.com/rss/edition_golf.rss', 'Golf'),
    ('http://rss.cnn.com/rss/edition_motorsport.rss', 'Motorsport'),
    ('http://rss.cnn.com/rss/edition_tennis.rss', 'Tennis'),
    ('http://rss.cnn.com/rss/edition_travel.rss', 'Travel'),
    ('http://rss.cnn.com/rss/cnn_freevideo.rss', 'Video'),
]
GTREND = [
    ('https://trends.google.com/trends/trendingsearches/daily/rss?geo=', 'US'),
]

def upd_dbnews():
    for rss in CNN:
        pars = parser.parse(*rss)
        news = parser.get_news(*pars)
        for post in news:
            try:
                Post.objects.create(
                    title=post['title'],
                    link=post['link'],
                    body=post['description'],
                    date_pub=post['pubdate'],
                    category=post['category'],
                )
            except Exception:
                continue
    return print('news done')


def upd_dbtrends():
    Trend.objects.all().delete()
    for trend in GTREND:
        url = trend[0] + trend[1]
        pars = parser.parse(url, trend[1])
        trends = parser.get_trends(*pars)
        for item in trends:
            try:
                Trend.objects.create(
                    title=item['trend'],
                    country=item['country'],
                )
            except Exception:
                continue
    return print('trends done')
