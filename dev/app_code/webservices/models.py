from __future__ import division
from __future__ import absolute_import

from app_code.config.config import DefaultConfig
import six.moves.urllib.request, six.moves.urllib.error, six.moves.urllib.parse
import six.moves.urllib.request, six.moves.urllib.parse, six.moves.urllib.error


current_domain = DefaultConfig.cookie_domain

def get_user_info():
    return {"status" : "success", "message" : "dict of userinfo"}
