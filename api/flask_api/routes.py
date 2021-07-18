# coding: UTF-8
"""
from flask import Flask, request, jsonify, Blueprint
from flask_cors import CORS
import sys
import os
import datetime
sys.path.append(os.path.abspath("../../"))
import api.flask_api.world_news.routes as pro

api = Flask(__name__)
CORS(api)

api.register_blueprint(pro)

@api.route('/api/npb/news/latestdate', methods=['GET'])
def latestdate():
    print(request.headers.get('Auth'))
    auth = request.headers.get('Auth')
    if not auth == nc.auth:
        return 'auth failed'
    #return_data = latest.main()
    return jsonify({'latest_news_date': return_data})

# おまじない
if __name__ == "__main__":
    api.run()
"""

# Flaskのインポート
from flask import Flask
from flask_cors import CORS
import sys
import os
sys.path.append(os.path.abspath("../../"))
#他モジュール(.py)のインポート
#from world_news.routes import world_news_api  #追加モジュール
from api.flask_api.world_news.routes import world_news_api

api = Flask(__name__)

CORS(api)
#他モジュール(.py)から呼び出す
api.register_blueprint(world_news_api)


#あとはレンダリング等の処理を記述
@api.route('/')
def login():
    return "HELLO"

if __name__ == "__main__":
    #api.run()
    api.run(debug=True)