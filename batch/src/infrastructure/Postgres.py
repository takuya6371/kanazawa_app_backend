import psycopg2

class Postgres:
    def __init__(self):
        self.sql_path = '/batch/src/sql/'
        self.con = psycopg2.connect(
            'host=' + '172.17.0.1' +
            ' port=' + '15432' +
            ' dbname=' + 'world_news' +
            ' user=' + 'kanazawa' +
            ' password=' + 'dockerkanazawa'
        )

    def read_sql_file (self, path):
        with open(path + '.sql', 'r') as f:
            file = f.read()
        return file

    '''
    def select_execute(self, sql):
        with self.con.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(sql)
            rows = cur.fetchall()

        return rows
    def get_crawl_url_list(self):
        sql =  'select * from crawl_urls'

        res = self.select_execute(sql)
        print(res)
        return res
    '''
