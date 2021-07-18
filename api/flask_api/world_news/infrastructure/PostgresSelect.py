import psycopg2
from psycopg2.extras import DictCursor
from api.flask_api.world_news.infrastructure import Postgres
import os

class PostgresSelect(Postgres.Postgres):
    def __init__(self):
        super(PostgresSelect, self).__init__()

    def select_execute(self, sql_file_name, search_params='', sort='', sort_col='',limit=100 ):
        clause, sql_params = self.make_clause(search_params, sort, sort_col, limit)
        sql = self.read_sql_file(
            self.sql_path + sql_file_name
        ) + clause
        with self.con.cursor(cursor_factory=DictCursor) as cur:
        #with self.con.cursor() as cur:
            cur.execute(sql, (sql_params))
            rows = cur.fetchall()
        #print(rows)
        return rows

    def select_news_list_translate(self, search_params, sort='desc', sort_col='date'):
        return self.select_execute(
            'select_news_list_translate',
            search_params,
            sort,
            sort_col
        )

    def select_news_list_original(self, search_params):
        return self.select_execute(
            'select_news_list_original',
            search_params
        )

    def select_country_list(self, search_params):
        return self.select_execute(
            'select_country_list',
            search_params
        )

    def select_site_list(self, search_params):
        return self.select_execute(
            'select_site_list',
            search_params
        )