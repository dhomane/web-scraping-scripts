import requests
from bs4 import BeautifulSoup


page = requests.get('http://www.cobbk12.org/schools/elementary_schools.aspx')

soup = BeautifulSoup(page.text, 'html.parser')

#print (soup.find('strong', text= '>​&#160'))


artist_name_list = soup.find_all(class_='col l2 large')
print(artist_name_list)
#artist_name_list_items = artist_name_list.find_all('a')


for artist_name_list_items in artist_name_list.find_all('a'):
    print (artist_name_list_items.get('href'))
#for artist_name in artist_name_list_items:
#    names = artist_name.contents[0]
#    print(names)
#for artist_name in artist_name_list_items:
#    print(artist_name.prettify())
