from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.poemas-del-alma.com/ruben-dario.htm')
bs = BeautifulSoup(html, "html.parser")

nameList = bs.findAll('ul', {'class': 'list-poems'})
for name in nameList:
    print(name.get_text())
