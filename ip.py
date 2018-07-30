import requests
import re
from bs4 import BeautifulSoup
url="http://whatismyip.host/"
data=requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
#print(data.content)
fhand=open("new.txt","w")
soup=BeautifulSoup(data.text, 'html.parser')
link=soup.find_all(id='ipv4')

s=str(link)
fhand.write(s)
