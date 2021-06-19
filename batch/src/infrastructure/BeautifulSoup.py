from bs4 import BeautifulSoup as bf
import requests

class BeautifulSoup:
    def __init__(self):
        self.ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)' \
        'AppleWebKit/537.36 (KHTML, like Gecko)' \
        'Chrome/60.0.3112.113'

    def getHtml (self, url: str, parser: str):
        html = requests.get(url, headers={"User-Agent": self.ua})
        return bf(html.content, parser)

    def run (self, url: str, parser = 'html.parser'):
        return self.getHtml(url, parser)
