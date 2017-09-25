# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+


import json
import requests
import uuid

from urlparse import urlparse

from flask_menu.classy import register_flaskview
from flask_menu.classy import classy_menu_item

from wazo_admin_ui.helpers.plugin import create_blueprint
from wazo_admin_ui.helpers.classful import BaseView
from wazo_admin_ui.helpers.form import BaseForm

from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, Length, Regexp


facebook = create_blueprint('facebook', __name__)
configfile = '/etc/facebook/config.json'

class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']

        FBView.service = FBService()
        FBView.register(facebook, route_base='/facebook')
        register_flaskview(facebook, FBView)

        core.register_blueprint(facebook)


class FBForm(BaseForm):
    page_access_token = StringField('Page Access Token', [InputRequired(), Length(max=256)])
    submit = SubmitField('Submit')


class FBView(BaseView):

    form = FBForm
    resource = 'facebook'

    @classy_menu_item('.facebook', 'Facebook', order=10, icon="facebook")
    def index(self):
        return super(FBView, self).get(None)

    def _map_resources_to_form(self, resource):
        page_access_token = resource.get('page_access_token')
        data = {
            'page_access_token': page_access_token
        }
        form = self.form(data=data)
        return form


class FBService(object):

    def get(self, arg):
        return self._read_config()

    def update(self, resource):
        config = self._read_config()
        config['page_access_token'] = resource.get('page_access_token')
        if not config.get('verify_token'):
            config['verify_token'] = str(uuid.uuid4().hex)

        with open(configfile, 'w') as outfile:
            json.dump(config, outfile, indent = 4)

        return True

    def _read_config(self):
        with open(configfile) as json_data:
            return json.load(json_data)
