# coding: UTF-8
import sys
import os
sys.path.append(os.path.abspath('../../../'))
print(os.getcwd())
from batch.src.usecase import CollectNews

if __name__ == '__main__':
    newsScrape = CollectNews.CollectNews()
    newsScrape.run()
