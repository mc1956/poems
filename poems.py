from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.poemas-del-alma.com/ruben-dario.htm')
bs = BeautifulSoup(html, "html.parser")

# the links :

for ultag in bs.find_all('ul', {'class': 'list-poems'}):
     for litag in ultag.find_all('li'):
             print(litag) #print (type(ultag.find_all('li')))

# find.All outputs an "array" ,
#so you have to loop through it to access the elements
# In this case we have only one ul f class "list-poems"
# so we can just select the first element like below

# The titles :

uls = bs.find_all('ul', {'class': 'list-poems'})[0]
for litag in uls.find_all('li'):
    print (litag.text)
