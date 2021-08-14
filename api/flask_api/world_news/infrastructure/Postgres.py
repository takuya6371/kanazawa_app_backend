import psycopg2
import os
class Postgres:
    def __init__(self):
        self.sql_path = 'flask_api/world_news/sql/'
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
            if 'start_' in key:
                key = key.split('start_')[1] + ' between %s'
            elif 'end_' in key:
                key = '%s'
            else:
                key = key +'=%s'
            clause = clause + (' where ' if clause == '' else ' and ') + key
            sql_params.append(value)
        print(clause)
        print(sql_params)
        if sort != '' and sort_col != '':
            clause = clause + ' order by ' + sort_col + ' ' + sort
        clause = clause + ' limit ' + str(limit)
        return clause, sql_params