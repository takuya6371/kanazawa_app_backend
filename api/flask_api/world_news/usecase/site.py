from flask_api.world_news.infrastructure import PostgresSelect
from flask_api.world_news.util.list import extractFromList

class Site:
    def __init__(self):
        self.select = PostgresSelect.PostgresSelect()

    def site_list(self, params):
        #select = PostgresSelect.PostgresSelect()
        #result = select.select_country_list(params)
        #return result
        return_value = []
        result = self.select.select_site_list(params)
        print(result)
        for val in result:
            return_value.append(extractFromList(val))
        return return_value
