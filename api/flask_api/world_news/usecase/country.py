from flask_api.world_news.infrastructure import PostgresSelect
from flask_api.world_news.util.list import extractFromList

class Country:
    def __init__(self):
        self.select = PostgresSelect.PostgresSelect()

    def country_list(self, params):
        #select = PostgresSelect.PostgresSelect()
        #result = select.select_country_list(params)
        #return result
        return_value = []
        result = self.select.select_country_list(params)
        for val in result:
            return_value.append(extractFromList(val))
        return return_value
