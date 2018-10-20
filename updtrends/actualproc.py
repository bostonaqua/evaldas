from updtrends.models import Post, Trend, ActualNews


def create_actual_posts():
    ActualNews.objects.all().delete()
    allnews = Post.objects.all()
    alltrends = Trend.objects.all()
    for post in allnews:
        for trend in alltrends:
            if trend.title.lower() in post.body:
                try:
                    ActualNews.objects.create(
                        title=post.title,
                        link=post.link,
                        date_pub=post.date_pub,
                        trend_name=trend.title,
                        category=post.category,
                        country=trend.country,
                        priority=1,
                    )
                except Exception:
                    continue
            splited_trend = trend.title.split()
            if len(splited_trend) > 1:
                for word in splited_trend:
                    if word.lower() not in post.body:
                        break
                else:
                    try:
                        ActualNews.objects.create(
                            title=post.title,
                            link=post.link,
                            date_pub=post.date_pub,
                            trend_name=trend.title,
                            category=post.category,
                            country=trend.country,
                            priority=2,
                        )
                    except Exception:
                        continue
    return print('created')