import requests
from bs4 import BeautifulSoup


page = requests.get('https://www.redclayschools.com/Domain/4')

soup = BeautifulSoup(page.text, 'html.parser')


artist_name_list = soup.find(class_='sw-dropdown-list')
#artist_name_list_items = artist_name_list.find_all('a')
for artist_name_list_items in artist_name_list.find_all('a'):
        element = str(artist_name_list_items.get_text())
        s = "Elementary"
        if s in element:
            print(element)

#print(artist_name_list_items)

#for artist_name_list_items in artist_name_list.find_all('a'):
#    final_artist_name_list_items = str(artist_name_list_items)
#    s = "Elementary"
#    if s in final_artist_name_list_items:
#        print("https://www.redclayschools.com"+artist_name_list_items.get('href'))
#for artist_name_list_items in artist_name_list.find_all('a'):
#    element = artist_name_list_items.get('href')
#    print (element)

#for artist_name in artist_name_list_items:
#    names = artist_name.contents[0]
#    print(names)
#for artist_name in artist_name_list_items:
#    print(artist_name)
#print(artist_name.prettify())
