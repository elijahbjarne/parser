import requests
from bs4 import BeautifulSoup

st_accept = "text/html"

st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"

headers = {
    "Accept": st_accept,
    "User-Agent": st_useragent
}

req = requests.get("https://thecode.media/parsing-2/")
src = req.text

soup = BeautifulSoup(src, 'lxml')

code = soup.find_all('code', 'language-python')
print(code)

#for link in soup.find_all('code', 'language-python'):
#    print(link.get('code'))