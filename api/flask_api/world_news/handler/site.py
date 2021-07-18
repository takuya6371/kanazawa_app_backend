from api.flask_api.world_news.infrastructure import PostgresSelect
from api.flask_api.world_news.usecase import site

class Site:
    def __init__(self):
        self.site = site.Site()

    def site_list(self, params):
        #select = PostgresSelect.PostgresSelect()
        #result = select.select_site_list(params)
        #return result
        return self.site.site_list(params)
