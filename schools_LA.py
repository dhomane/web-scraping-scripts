import requests
from bs4 import BeautifulSoup


page = requests.get('https://achieve.lausd.net/Page/14358')

soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify())

artist_name_list = soup.find(class_='hidden-section')
#artist_name_list_items = artist_name_list.find_all('a')
#print(artist_name_list_items)
for artist_name_list_items in artist_name_list.find_all('a'):
    print (artist_name_list_items)

#for artist_name in artist_name_list_items:
 #   names = artist_name.contents[0]
  #  print(names)
#for artist_name in artist_name_list_items:
#    print(artist_name)
#print(artist_name.prettify())
