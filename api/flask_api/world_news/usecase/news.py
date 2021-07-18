# coding: UTF-8
from api.flask_api.world_news.infrastructure import PostgresSelect
from api.flask_api.world_news.util.list import extractFromList

class News:
    def __init__(self):
        self.select = PostgresSelect.PostgresSelect()

    def news_list_translate(self, params):
        #select = PostgresSelect.PostgresSelect()
        return_value = []
        result = self.select.select_news_list_translate(params)
        for val in result:
            return_value.append(extractFromList(val))
        return return_value

    def news_list_original(self, params):
        #select = PostgresSelect.PostgresSelect()
        result = self.select.select_news_list_original(params)
        return result