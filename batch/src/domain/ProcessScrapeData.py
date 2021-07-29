import traceback
from batch.src.infrastructure import GoogleTrans
from batch.src.infrastructure import BeautifulSoup
from batch.src.infrastructure import PostgresInsert
from batch.src.infrastructure import PostgresSelect
from batch.src.util import Day
import re

site_url = 'site_url'
target_page_url = 'target_page_url'
article_url_keyword = 'article_url_keyword'
article_title_tag_key_list = 'article_title_tag_key_list'
article_content_tag_key_list = 'article_content_tag_key_list'
article_genre_tag_key_list = 'article_genre_tag_key_list'
href_type_divide = 0

class ProcessScrapeData:
    def __init__(self):
        self.googleTrans = GoogleTrans.GoogleTrans()
        self.beautifulSoup = BeautifulSoup.BeautifulSoup()
        self.PostgresSelect = PostgresSelect.PostgresSelect()
        self.PostgresInsert = PostgresInsert.PostgresInsert()
        self.p = re.compile(r'<[^>]*?>')


    def extract_a_tags(self, scrape_data):
        return scrape_data.find_all('a')

    def extract_article_elem(self, url):
        return self.beautifulSoup.run(url)

    def is_article_url(self, url, article_soup, article_keyword_type, article_keyword):
        result = True
        if article_keyword_type == 'url':
            result = url is not None and article_keyword in url
        elif article_keyword_type == 'html_find':
            result = len(article_soup.select(article_keyword)) > 0

        print(result)
        if result == False:
            self.PostgresInsert.insert_exclude_urls(url)

        return result

    def extract_target_data(
        self,
        target_soup,
        article_tag_key_list,
    ):
        current_tag = None
        for article_tag_key in article_tag_key_list:
            if article_tag_key[0] == 'split':
                # if split imidiate return
                split_index = int(article_tag_key[2])
                current_tag = target_soup.text.split(article_tag_key[1]) if current_tag is None else current_tag.text.split(article_tag_key[1])[split_index]
                return current_tag
            else:
                select_index = int(article_tag_key[1])
                if select_index > 0:
                    current_tag = target_soup.find_all(article_tag_key[0])[select_index] if current_tag is None else current_tag.find_all(article_tag_key[0])[select_index]
                else:
                    print(current_tag is None)
                    current_tag = target_soup.select_one(article_tag_key[0]) if current_tag is None else current_tag.select_one(article_tag_key[0])
        return self.p.sub('', current_tag.text)

    def transrate(self, text):
        return self.googleTrans.run(text)

    def registor_article(self, article_info, url_info):
        self.PostgresInsert.article_transaction(article_info, url_info)

    def extract_target_tag(self, soup, target_tags):
        tags = []
        for tag in target_tags:
            target_tag = soup.select_one(tag)
            tags.extend(self.extract_a_tags(target_tag))
        return tags

    def run (self, url_info):
        try:
            a_tags = []
            url_soup = self.beautifulSoup.run(url_info['site_url'] + url_info['target_page_url'])
            a_tags = self.extract_target_tag(url_soup, url_info['target_tag'])
            for a_tag in list(set(a_tags)):
                #print(a_tag.get('href'))
                try:
                    article_info = {}
                    print(a_tag)
                    print(url_info['hrefs_type'])
                    print(a_tag.get('href'))
                    print(url_info['site_url'])
                    url = url_info['site_url'] + '/' + a_tag.get('href') if url_info['hrefs_type'] == href_type_divide else a_tag.get('href')
                    print(url)
                    if a_tag.get('href') is not None and len(self.PostgresSelect.select_article_url(url)) == 0 and len(self.PostgresSelect.select_exclude_urls(url)) == 0:
                        article_soup = self.extract_article_elem(url)
                        if self.is_article_url(url, article_soup, url_info['article_keyword_type'], url_info['article_keyword']):
                            article_info['url'] = url
                            article_info['genre'] = self.extract_target_data(
                                article_soup,
                                url_info['article_genre_tag_key_list'],
                            )
                    
                            article_info['title'] = self.extract_target_data(
                                article_soup,
                                url_info['article_title_tag_key_list'],
                            )
                            article_info['content'] = self.extract_target_data(
                                article_soup,
                                url_info['article_content_tag_key_list'],
                            )
                            date = self.extract_target_data(
                                article_soup,
                                url_info['article_date_tag_key_list'],
                            )
                            article_info['date'] = date if Day.checkDate(date) else Day.get_today('%Y-%m-%d')
                            try:
                                article_info['trans_genre'] = self.transrate(article_info['genre'])
                                article_info['trans_title'] = self.transrate(article_info['title'])
                                article_info['trans_content'] = self.transrate(article_info['content'])
                            except Exception as e:
                                print('fail trans')
                                raise
                                
                            #print(title)
                            #print(trans_title)
                            #print(trans_content)
                            self.registor_article(article_info, url_info)
                    else:
                        if a_tag.get('href') is not None:
                            print('already registered:'+a_tag.get('href'))
                except Exception as e:
                    print(e)
                    traceback.print_exc()
                    if a_tag.get('href') is not None:
                        print('skip:'+a_tag.get('href'))
                    continue    
        except Exception as e:
            raise