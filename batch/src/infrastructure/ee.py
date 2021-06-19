from bs4 import BeautifulSoup as bf
import requests

ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)" \
     "AppleWebKit/537.36 (KHTML, like Gecko)" \
     "Chrome/60.0.3112.113"

res = requests.get('https://postcourier.com.pg/', headers={"User-Agent": ua})
print('res_url: ', res.content)
print('res_url: ', res.status_code)