import json
import os
import sys

from staticjinja import Site


if __name__ == "__main__":
    news_file_path = os.path.join(os.path.dirname(__file__), 'contents/news.json')
    news_context = json.loads(open(news_file_path).read())
    news_context = sorted(news_context, key=lambda x: x.get('date'))
    context = {
        'news': news_context
    }

    site = Site.make_site(contexts=[
        ('index.html', context),
    ])
    site.render(use_reloader=int(sys.argv[1]) == 1 if len(sys.argv) > 1 else False)
