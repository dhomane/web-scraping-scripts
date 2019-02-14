import urllib.request
from bs4 import BeautifulSoup

quote_page = "https://en.wikipedia.org/wiki/Atlanta_Public_Schools"
#page = urllib2.urlopen(quote_page)

request = urllib.request.Request(quote_page)
response = urllib.request.urlopen(request)

# parse the html using beautiful soup and store in variable `soup`
#soup = BeautifulSoup(page, 'html.parser')
soup = BeautifulSoup(response, 'html.parser')

print(soup.prettify())
