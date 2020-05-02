from __future__ import absolute_import
import datetime
from flask import (Blueprint, request,make_response, abort, render_template, g)
import six.moves.urllib.request, six.moves.urllib.parse, six.moves.urllib.error
from . import models as Models
import json

webservices = Blueprint('webservices', __name__)

@webservices.route('/get_user_info',methods=['GET', 'POST'])
def get_user_info():
    user_info = Models.get_user_info()
    json_response = json.dumps(user_info, default=str)
    response = make_response(json_response)
    response.headers['Content-Type'] = 'application/json'
    return response



