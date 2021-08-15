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
from flask import Flask, send_file
from flask_cors import CORS
import sys
import os
sys.path.append(os.path.abspath("../"))
from flask_api.world_news.routes import world_news_api

# 他モジュール(.py)のインポート
# from world_news.routes import world_news_api  #追加モジュール

api = Flask(__name__)

CORS(api)
# 他モジュール(.py)から呼び出す
api.register_blueprint(world_news_api)


# あとはレンダリング等の処理を記述
@api.route('/')
def login():
    return "HELLO"

@api.route('/.well-known/acme-challenge/3NC3Q0NIfMkQ1Q8g8ngTVSxb5tPgjBQ1cA0WMA0_o1Y')
def test():
    filepath = "./3NC3Q0NIfMkQ1Q8g8ngTVSxb5tPgjBQ1cA0WMA0_o1Y"
    filename = os.path.basename(filepath)
    return send_file(filepath, as_attachment=True,
                     attachment_filename=filename,
                     mimetype='text/plain')

if __name__ == "__main__":
    #api.run()
    api.run(debug=True)
