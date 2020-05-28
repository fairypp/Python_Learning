import urllib.error, urllib.request, urllib.parse
from bs4 import BeautifulSoup
a = int(input("Position: "))-1
b = int(input("Times: "))
url = input("Enter URL: ")

for c in range(b):
    html= urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    d = tags[a].get('href',None)
    url=d
    e = tags[a].contents[0]
print(e)
