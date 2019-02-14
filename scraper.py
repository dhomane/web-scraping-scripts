# import libraries
import urllib.request
from bs4 import BeautifulSoup

quote_page = "https://en.wikipedia.org/wiki/Atlanta_Public_Schools"
#page = urllib2.urlopen(quote_page)

request = urllib.request.Request(quote_page)
response = urllib.request.urlopen(request)

# parse the html using beautiful soup and store in variable `soup`
#soup = BeautifulSoup(page, 'html.parser')
soup = BeautifulSoup(response, 'html.parser')

#print(soup.prettify())

all_links = soup.find_all("a")
for link in all_links:
    print (link.get("href"))

right_table = soup.find_all('table',class_= 'nowraplinks collapsible autocollapse navbox-inner')

school_list = []
for row in right_table.find_all('li'):
    for r in find('row',class_= 'toclevel-2 tocsection-7'):
        school_list.append(r)

print(school_list)
