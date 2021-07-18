import psycopg2

class Postgres:
    def __init__(self):
        self.sql_path = 'world_news/sql/'
        self.con = psycopg2.connect(
            'host=' + 'postgres_db' +
            ' port=' + '5432' +
            ' dbname=' + 'world_news' +
            ' user=' + 'kanazawa' +
            ' password=' + 'dockerkanazawa'
        )

    def read_sql_file (self, path):
        with open(path + '.sql', 'r') as f:
            file = f.read()
        return file

    def make_clause (self, params, sort, sort_col, limit):
        sql_params = []
        clause = ''
        for i, (key, value) in enumerate(params.items()):
            print(key)
            print(value)
            clause = clause + (' where ' if clause == '' else ' ') + key +'=%s' 
            sql_params.append(value)
        print(clause)
        print(sql_params)
        if sort != '' and sort_col != '':
            clause = clause + ' order by ' + sort_col + ' ' + sort
        clause = clause + ' limit ' + str(limit)
        return clause, sql_params