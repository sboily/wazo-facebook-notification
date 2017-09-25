# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+


import os
import json

from flask import request, make_response
from flask_restful import Resource

from fbmessenger import BaseMessenger


configfile = '/etc/facebook/config.json'


class Messenger(BaseMessenger):
    def __init__(self, page_access_token):
        self.page_access_token = page_access_token
        super(Messenger, self).__init__(self.page_access_token)

    def message(self, message):
        self.send({'text': 'Received: {0}'.format(message['message']['text'])})

    def delivery(self, message):
        pass

    def read(self, message):
        pass

    def account_linking(self, message):
        pass

    def postback(self, message):
        pass

    def optin(self, message):
        pass


class FBResource(Resource):
    def __init__(self):
        self.messenger = Messenger(self._get_page_access_token())

    def get(self):
        print(self._get_verify_token())
        if (request.args.get('hub.verify_token') == self._get_verify_token()):
            return make_response(request.args.get('hub.challenge'))
        return {'error': 'VERIFY_TOKEN does not match'}, 401

    def post(self):
        self.messenger.handle(request.get_json(force=True))

    def _get_verify_token(self):
        with open(configfile) as json_data:
            config = json.load(json_data)

        return config['verify_token']

    def _get_page_access_token(self):
        with open(configfile) as json_data:
            config = json.load(json_data)

        return config['page_acces_token']
