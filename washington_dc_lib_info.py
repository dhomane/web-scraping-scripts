import requests
from bs4 import BeautifulSoup
#from google import google

page = requests.get('http://profiles.dcps.dc.gov/')

soup = BeautifulSoup(page.text, 'html.parser')

content = soup.find('tbody')

web_list = content.find_all("a", string="Website")

site_list=[]
for site in web_list:
    site_list.append(site.get('href'))
    

#print(site_list)


var = ' Staff'

site_list_new = [ x + var for x in site_list ]

#print(site_list_new)

try:
	from googlesearch import search
except ImportError: 
	print("No module named 'google' found")

# Using Google Search Python API to iteratively search for links containing Staff Information
# In most of the cases the top 3 search results found the staff directory information.

print("List of URLs containing Staff Contacts")
print(" ")
for i in site_list_new:
    
    query = i
    for j in search(query, tld="com", num=3, stop=1, pause=2):
        print(j)
    print("--------------------------")

# Once we get the link containing staff list, use a BeautifulSoup function to parse for strings like Librarian, Library Media Specialist etc
	
