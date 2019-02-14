import requests
from bs4 import BeautifulSoup


page = requests.get("https://www.wcpss.net/")

soup = BeautifulSoup(page.text, 'html.parser')


artist_name_list = soup.find(class_='sw-dropdown-list')

artist_name_list_items = artist_name_list.find_all('a')

for artist_name_list_items in artist_name_list.find_all('a'):
    s = "Elementary"
    element = str(artist_name_list_items)
    if s in element:
        print("https://www.wcpss.net"+artist_name_list_items.get("href"))
        #print(artist_name_list_items.get_text())


#for artist_name in artist_name_list_items:
 #   names = artist_name.contents[0]
  #  print(names)
#for artist_name in artist_name_list_items:
#    print(artist_name)
#print(artist_name.prettify())
