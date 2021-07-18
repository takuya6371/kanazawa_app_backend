# coding: UTF-8
from flask import Flask, Blueprint, jsonify, request
from api.flask_api.world_news.handler import news
from api.flask_api.world_news.handler import country
from api.flask_api.world_news.handler import site
import traceback

#import sys
#import os
#sys.path.append(os.path.abspath("../../"))

#Blueprintでモジュールの登録
world_news_api = Blueprint('world_news', __name__, url_prefix='/world_news')

#レンダリング処理を記述
@world_news_api.route('/news_list_translate', methods=['GET'])
def news_list_translate():
    try:
        req = request.args
        newsClass = news.News()
        result = newsClass.news_list_translate(request.args)
        return jsonify({'data': result})
    except Exception as e:
        traceback.print_exc()

@world_news_api.route('/news_list_original', methods=['GET'])
def news_list_original():
    try:
        req = request.args
        newsClass = news.news()
        result = newsClass.news_list_original(request.args)
        return jsonify({'data': result})
    except Exception as e:
        traceback.print_exc()

@world_news_api.route('/country_list', methods=['GET'])
def country_list():
    try:
        req = request.args
        countryClass = country.Country()
        result = countryClass.country_list(request.args)
        return jsonify({'data': result})
    except Exception as e:
        traceback.print_exc()

@world_news_api.route('/site_list', methods=['GET'])
def site_list():
    try:
        req = request.args
        siteClass = site.Site()
        result = siteClass.site_list(request.args)
        return jsonify({'data': result})
    except Exception as e:
        traceback.print_exc()