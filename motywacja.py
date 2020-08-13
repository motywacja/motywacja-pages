import json

from staticjinja import Site

if __name__ == "__main__":
    news_context = json.loads(open('contents/news.json').read())
    news_context = sorted(news_context, key=lambda x: x.get('date'))
    context = {
        'news': news_context
    }

    site = Site.make_site(contexts=[
        ('index.html', context),
    ])
    site.render(use_reloader=True)
