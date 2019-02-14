import requests
from bs4 import BeautifulSoup


page = requests.get('https://www.atlantapublicschools.us/Page/54020')

soup = BeautifulSoup(page.text, 'html.parser')



artist_name_list = soup.find(class_='sw-dropdown-list')
artist_name_list_items = artist_name_list.find_all('a')

for artist_name_list_items in artist_name_list.find_all('a'):
    print ('https://www.atlantapublicschools.us' + artist_name_list_items.get('href'))
#for artist_name in artist_name_list_items:
#    names = artist_name.contents[0]
#    print(names)
#for artist_name in artist_name_list_items:
#    print(artist_name.prettify())
