import os
from bs4 import BeautifulSoup
file_path = 'data/1.html'

html = open(file_path, 'rt').read()

soup = BeautifulSoup(html, 'lxml')

print(soup.title.parent.name)

for link in soup.find_all('p'):
    print(link)