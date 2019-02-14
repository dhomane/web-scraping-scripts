import requests
from bs4 import BeautifulSoup


page = requests.get('http://publish.gwinnett.k12.ga.us/gcps/home/public/schools')

soup = BeautifulSoup(page.text, 'html.parser')

#print (soup.find('strong', text= '>​&#160'))

artist_name_list = soup.find_all(class_='col-md-3 col-sm-6 col-xs-11')
#print(artist_name_list)
#artist_name_list_items = artist_name_list.find_all('a')


for artist_name_list_items in artist_name_list.find_all('a'):
    print (artist_name_list_items.get('href'))
#for artist_name in artist_name_list_items:
#    names = artist_name.contents[0]
#    print(names)
#for artist_name in artist_name_list_items:
#    print(artist_name.prettify())
