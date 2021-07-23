# coding: UTF-8
from flask_api.world_news.usecase import news

class News:
    def __init__(self):
        self.news = news.News()

    def news_list_translate(self, params):
        #select = PostgresSelect.PostgresSelect()
        return self.news.news_list_translate(params)

    def news_list_original(self, params):
        #select = PostgresSelect.PostgresSelect()
        return self.news.news_list_original(params)