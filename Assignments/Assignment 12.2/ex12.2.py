import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter first url : ')
position = int(input('Enter position : '))
count = int(input('Enter count : '))
link = None

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')

# print(tags[position - 1].get('href', None))
# print(tags[position - 1].contents[0])

while count > 1 :
    html = urllib.request.urlopen(tags[position - 1].get('href', None)).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')

    # print(tags[position - 1].get('href', None))
    name = tags[position - 1].contents[0]
    count = count - 1
print(name)