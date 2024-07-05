import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

filehandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for line in filehandle:
    print(line.decode().strip())
newFile = urllib.request.urlopen('http://dr-chuck.com/page1.htm', context=ctx)
html = newFile.read()
soup = BeautifulSoup(html, 'html.parser')
print(soup)

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
# But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief