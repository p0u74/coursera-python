import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter url : ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
sum = 0
for tag in tags :
    num = tag.contents[0]
    sum = sum + int(num)
print(sum)