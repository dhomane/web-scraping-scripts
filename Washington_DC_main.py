import requests
from bs4 import BeautifulSoup


page = requests.get('http://profiles.dcps.dc.gov/')

soup = BeautifulSoup(page.text, 'html.parser')

content = soup.find('tbody')


#List of School Names
school_list = content.find_all(class_='school_name')

for name in school_list:
	print(name.text)

print("------------------------------------------") # Separator line
# List of School Websites
web_list = content.find_all("a", string="Website")

for site in web_list:
    print(site.get('href'))
    
print("------------------------------------------") # Separator line
    
#List of Principal Names
    
princy_list = content.find_all(class_='principal_name')

for p in princy_list:
    princy = p.find('a')
    print(princy.text)


print("------------------------------------------") # Separator line
#List of Principal Emails

links_list = content.find_all(class_='principal_name')

links=[]

for item in links_list:
    for l in item.find_all('a'):
        links.append(l.get('href'))
        
for u in links:
    print(u[7:])
    
print("------------------------------------------") # Separator line
#List of School Addresses
    
content_list = soup.findAll(True, {'class':['tr_odd filter-in', 'tr_even filter-in']})

details=[]

for info in content_list:
    details.append(info.text)
    
add=[]

for z in details:
    lines_add = z.splitlines()
    add.append(lines_add[3])
    
for address in add:
    print(address.replace("Washington", ", Washington"))
    
print("------------------------------------------") # Separator line
#List of Phone Numbers    

num=[]

for y in details:
    lines_num = y.splitlines()
    num.append(lines_num[4])
    
for number in num:
    print(number[:14])

    

    

    
    
    



    

    
            
            
    
