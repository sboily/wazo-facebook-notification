# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from .resource import FBResource


class Plugin(object):

    def load(self, dependencies):
        api = dependencies['api']
        api.add_resource(FBResource, '/facebook')
