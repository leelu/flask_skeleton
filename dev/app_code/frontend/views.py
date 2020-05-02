from __future__ import absolute_import
from flask import (Blueprint, render_template, request, make_response,
                   redirect, url_for, g, flash, jsonify, abort, session,send_from_directory, current_app)
from app_code.config.config import DefaultConfig as DefaultConfig
import json
import time
import requests
import six.moves.urllib.request, six.moves.urllib.parse, six.moves.urllib.error


current_domain = DefaultConfig.cookie_domain
frontend = Blueprint('frontend', __name__, template_folder='templates')

@frontend.route('/',methods=['GET', 'POST'])
def index():
    try:
        result = {"user_name" : "leela", "message" : "welcome to domain " + DefaultConfig.cookie_domain}
        return make_response(render_template(current_domain + '/home_page.html',data=result))
    except Exception as e:
        return make_response(e.message, 200)



