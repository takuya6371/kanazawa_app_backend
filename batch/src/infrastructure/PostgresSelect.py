import psycopg2
from psycopg2.extras import DictCursor
from batch.src.infrastructure import Postgres

class PostgresSelect(Postgres.Postgres):
    def __init__(self):
        super(PostgresSelect, self).__init__()

    def select_execute(self, sql, params = ''):
        with self.con.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(sql, (params))
            rows = cur.fetchall()
        return rows

    def select_crawl_url_list(self):
        return self.select_execute(self.read_sql_file(self.sql_path + 'select_crawl_url_list'))

    def select_exclude_urls(self, url):
        return self.select_execute(
            self.read_sql_file(self.sql_path + 'select_exclude_urls'),
            [url]
        )

    def select_article_url(self, url):
        return self.select_execute(
            self.read_sql_file(self.sql_path + 'select_article_url'),
            [url]
        )

#aa = Postgres()
#aa.get_crawl_url_list()