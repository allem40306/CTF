import re
import requests
from bs4 import BeautifulSoup

header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"}

for page in range(0, 1000):
    url = "http://chals1.ais3.org:8987/bear/%d"%(page)
    r = requests.get(url,headers=header)
    soup = BeautifulSoup(r.text, 'html.parser')
    for item in soup.find_all('h3'):
        print(page, item.text)
