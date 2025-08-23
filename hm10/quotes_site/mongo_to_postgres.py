import pymongo
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotes_site.settings')
django.setup()

from quotes.models import Author, Quote
from django.contrib.auth.models import User

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mongo_quotes']

default_user = User.objects.first() or User.objects.create_user('default', 'default@site.com', 'password')

for a in db.authors.find():
    author, _ = Author.objects.get_or_create(
        fullname=a['fullname'],
        defaults={
            'born_date': a.get('born_date', ''),
            'born_location': a.get('born_location', ''),
            'description': a.get('description', ''),
        }
    )

for q in db.quotes.find():
    author = Author.objects.get(fullname=q['author'])
    Quote.objects.get_or_create(
        text=q['quote'],
        author=author,
        defaults={
            'tags': ', '.join(q.get('tags', [])),
            'created_by': default_user,
        }
    )
