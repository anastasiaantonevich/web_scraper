import requests
from bs4 import BeautifulSoup, SoupStrainer

page = 'https://uchi.ru'

r = requests.get(page)
print(r.url , ":", r.status_code, r.status_code == requests.codes.ok)
# Create a BeautifulSoup object
soup = BeautifulSoup(r.content, 'html.parser', parse_only=SoupStrainer('a'))
pages = [link['href'] for link in soup if link.get('href')]

filter_pages = []
for link in pages:
    if link.startswith('/') and not link.startswith ('//') and not link.startswith('tel'):
        link = page + link
        filter_pages.append(link)
        print(link, ':', requests.get(link).status_code)
