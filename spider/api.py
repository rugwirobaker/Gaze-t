import os, sys

app_path = 'C:\\Users\\22tk\\Desktop\\workspace\\GatorReview'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GatorReview.settings')
sys.path.append(app_path)
os.chdir(app_path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from news.models import Article

def create_new_article(data):
    #task unstage dictionnary
    new_article = Article()
    new_article.title = data['title']
    new_article.author = data['author']
    new_article.publication_date = data['publication_date']
    new_article.summary = data['summary']
    new_article.article_image = data['image_url']
    new_article.article_url = data['article_url']
    new_article.save()
