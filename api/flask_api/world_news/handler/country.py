from api.flask_api.world_news.infrastructure import PostgresSelect
from api.flask_api.world_news.usecase import country

class Country:
    def __init__(self):
        self.country = country.Country()

    def country_list(self, params):
        #select = PostgresSelect.PostgresSelect()
        #result = select.select_country_list(params)
        #return result
        return self.country.country_list(params)
