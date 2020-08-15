import json
import math
import os
import sys

from staticjinja import Site


if __name__ == "__main__":
    news_file_path = os.path.join(os.path.dirname(__file__), 'contents/news.json')
    contacts_file_path = os.path.join(os.path.dirname(__file__), 'contents/contacts.json')
    about_file_path = os.path.join(os.path.dirname(__file__), 'contents/about.json')
    footer_file_path = os.path.join(os.path.dirname(__file__), 'contents/footer.json')

    footer_context = json.loads(open(footer_file_path).read())

    news = json.loads(open(news_file_path).read())
    news = sorted(news, key=lambda x: x.get('date'))
    pages = math.ceil(len(news) / 20)
    news = news[:20]
    main_context = {
        'news': news,
        'pages': pages
    }

    contact_context = json.loads(open(contacts_file_path).read())

    about_context = json.loads(open(about_file_path).read())

    all_views_contexts = [main_context, contact_context, about_context]
    for context in all_views_contexts:
        context['footer'] = footer_context

    site = Site.make_site(contexts=[
        ('index.html', main_context),
        ('about.html', about_context),
        ('contact.html', contact_context)
    ])
    site.render(use_reloader=int(sys.argv[1]) == 1 if len(sys.argv) > 1 else False)
