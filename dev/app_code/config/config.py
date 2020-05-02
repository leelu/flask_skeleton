from __future__ import absolute_import
__author__ = 'leela'
import os
class BaseConfig(object):
    PROJECT = "app_code"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    TESTING = False
    SSL = 'https'
    TOKEN_EXPIRY = 3600
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or 'aaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbccccccccccccccc111111111111'


class DefaultConfig(BaseConfig):
    COUNTRY_CODE = 'US'
    LOG_FILE_PATH = '/var/www/chatur/dev/logs'
    DEBUG = False
    cookie_domain = 'chatur.myyogateacher.com'
