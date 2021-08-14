# coding: UTF-8
from batch.src.infrastructure import BeautifulSoup
from batch.src.infrastructure import PostgresSelect
from batch.src.domain import ProcessScrapeData
import re
import traceback

class CollectNews:
    def __init__(self):
        self.ProcessScrapeData = ProcessScrapeData.ProcessScrapeData()
        self.beautifulSoup = BeautifulSoup.BeautifulSoup()
        self.postgresSelect = PostgresSelect.PostgresSelect()

    def get_data(self):
        return self.postgresSelect.select_crawl_url_list()

    def run(self):
        try:
            url_info_list = self.get_data()
            print(url_info_list)
            for url_info in url_info_list:
                self.ProcessScrapeData.run(url_info)
        except Exception as e:
            traceback.print_exc()
