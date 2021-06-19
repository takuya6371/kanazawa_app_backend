"""
from googletrans import Translator
class GoogleTrans:
    def __init__(self):
        self.translator = Translator(service_urls=['translate.googleapis.com'])

    def run (self, word, src='en', dest='ja'):
        text = ''
        while True:
            try:
                print(self.translator.translate(word, src=src, dest=dest))
                text = self.translator.translate(word, src=src, dest=dest).text
                break
            except Exception as e:
                self.translator = Translator(service_urls=['translate.googleapis.com'])
        return text
"""
import argparse
import requests
import pprint
import json

class GoogleTrans:
    def __init__(self):
        #self.translator = Translator(service_urls=['translate.googleapis.com'])
        self.api_url = "https://script.google.com/macros/s/AKfycbwU91N2hssRUVvBel9SsHTLUpySPLghCWh30tw3Xg4p8vDNv3PCZx7apgFkiaQksIh6QA/exec"
        self.headers = {"Authorization": "Bearer ya29.a0AfH6SMBH-VoLGkSFdDBwDnH_TaxGNS2pAoy4XLOcftiervyuZLsLZ1RV3AoTULSz8maRE6vWgzyW-WB7Ans0ZfyWNBSou4RZstL509BIvLJJtWJflDIwUB44tsrxw4iVvApMEUMExCkEHFtpb7Anc4ltHjHa"}

    def run (self, word, src='en', dest='ja'):

        #word = "We just want quarantine facilities revived - MFA"

        params = {
            'text': "\"" + word + "\"",
            'source': src,
            'target': dest,
        }
        try:
            r_post = requests.post(self.api_url, headers=self.headers, data=params)
            response = json.loads(r_post.text)
            if not response['code'] == 200:
                raise 'trans code error:' + response['code']
            return response['text']
        except Exception as e:
            print("trans error")
            print(e)
            raise

