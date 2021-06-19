import psycopg2
from psycopg2.extras import DictCursor
from batch.src.infrastructure import Postgres

class PostgresInsert(Postgres.Postgres):
    def __init__(self):
        super(PostgresInsert, self).__init__()

    def insert_execute(self, sql:str, params:list):
        cur = self.con.cursor()
        cur.execute(sql,(params))
        cur.execute('SELECT LASTVAL()')
        #print(cur.fetchone()[0])
        return cur.fetchone()[0]


    def insert_news_list_original(self:str, site_id:str, country:str, date:str, url:str, title:str, genre:str, content:str):
        return self.insert_execute(
            self.read_sql_file(self.sql_path + 'insert_news_list_original'),
            [site_id,country,date,url,genre,title,content]
        )

    def insert_news_list_translate(self:str, site_id:str, original_id:str, country:str, date:str, url:str, title:str, genre:str, content:str):
        self.insert_execute(
            self.read_sql_file(self.sql_path + 'insert_news_list_translate'),
            [site_id,original_id,country,date,url,genre,title,content]
        )

    def insert_exclude_urls(self:str, url:str):
        self.insert_execute(
            self.read_sql_file(self.sql_path + 'insert_exclude_urls'),
            [url]
        )
        self.con.commit()

    def article_transaction(self, article_info:dict, url_info:dict):
        #print(article_info, url_info)
        try:
            last_id = self.insert_news_list_original(
                url_info['id'],
                url_info['country'],
                article_info['date'],
                article_info['url'],
                article_info['title'],
                article_info['genre'],
                article_info['content'],
            )
            print(last_id)

            self.insert_news_list_translate(
                url_info['id'],
                last_id,
                url_info['country'],
                article_info['date'],
                article_info['url'],
                article_info['trans_title'],
                article_info['trans_genre'],
                article_info['trans_content'],
            )

            self.con.commit()
        except Exception as e:
            self.con.rollback()
            raise
        return 'res'

