#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from setuptools import find_packages
from setuptools import setup

setup(
    name='wazo_facebook_notifier',
    version='0.1',

    description='Wazo Facebook notifier',

    author='Wazo Authors',
    author_email='dev@wazo.community',

    url='http://wazo.community',

    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    package_data={
        'facebook_admin_ui': ['templates/*/*.html'],
    },

    entry_points={
        'wazo_admin_ui.plugins': [
            'facebook = facebook_admin_ui.plugin:Plugin',
        ],
        'wazo_webhookd.plugins': [
            'facebook = facebook_webhookd.plugin:Plugin',
        ]
    }
)
