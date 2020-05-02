__author__ = 'leela'
  
from flask import Flask, render_template, Blueprint, request, redirect, url_for, g, session
from flask_wtf.csrf import CSRFProtect,CSRFError
from app_code.config.config import DefaultConfig as DefaultConfig
from .frontend import frontend
from .webservices import webservices
import datetime
# For import *
__all__ = ['create_app']

# tuple of blue prints to register
DEFAULT_BLUEPRINTS = (
    frontend, webservices
)

import os
INSTANCE_FOLDER_PATH = os.path.join('/tmp', 'instance')

csrf = CSRFProtect()

def create_app(config=None, app_name=None, blueprints=None):
    """Create a Flask app.
    :param config: app_config_object
    :param app_name: application name
    :param blueprints: a tuple containing required blueprints
    """

    if app_name is None:
        app_name = DefaultConfig.PROJECT
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(app_name, instance_path=INSTANCE_FOLDER_PATH,
                instance_relative_config=True, template_folder='templates')
    
    configure_app(app, config)
    app.config['SECRET_KEY'] = DefaultConfig.SECRET_KEY
    app.config['SESSION_COOKIE_DOMAIN'] = DefaultConfig.cookie_domain
    app.config['SESSION_COOKIE_SECURE'] = False
    app.jinja_options['extensions'].append('jinja2.ext.do')
    app.jinja_env.add_extension('jinja2.ext.loopcontrols')
    configure_hook(app)
    configure_blueprints(app, blueprints)
    configure_extensions(app)
    configure_logging(app)
    configure_template_filters(app)
    configure_error_handlers(app)
    app.config.update(
        DEBUG=True,
        TEMPLATE_DEBUG=True,
    )
    return app


def configure_app(app, config=None):
    """Different ways of configurations.
    :param app:object
    :param config:object
    """

    # http://flask.pocoo.org/docs/api/#configuration
    app.config.from_object(DefaultConfig)

    # http://flask.pocoo.org/docs/config/#instance-folders
    app.config.from_pyfile('production.cfg', silent=True)


    if config:
        app.config.from_object(config)

    # Use instance folder instead of env variables to make deployment easier.
    #app.config.from_envvar('%s_APP_CONFIG' % DefaultConfig.PROJECT.upper(), silent=True)


def configure_extensions(app):
    csrf.init_app(app)
    csrf.exempt(webservices)


def configure_blueprints(app, blueprints):
    """Configure blueprints in views.
    :param app:
    :param blueprints:
    """

    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_template_filters(app):
    """
    add any custom filters required in jinja
    :param app: application context object
    :return:formatted date time
    """

    @app.template_filter()
    def pretty_date(value):
        return pretty_date(value)

    @app.template_filter()
    def format_date(value, format='%Y-%m-%d'):
        return value.strftime(format)

def configure_hook(app):
    @app.before_request
    def before_request():
        g.root_path = DefaultConfig.PROJECT_ROOT

def configure_logging(app):
    pass

def configure_error_handlers(app):
    """
    Handle HTTP error codes
    :param app:
    :return:
    """
    current_domain = DefaultConfig.cookie_domain

    @app.errorhandler(400)
    def forbidden_page(error):
        return render_template(
            current_domain + "/errors/forbidden_page.html"), 400

    @app.errorhandler(401)
    def forbidden_page(error):
        return render_template(
            current_domain + "/errors/forbidden_page.html"), 401

    @app.errorhandler(405)
    def forbidden_page(error):
        return render_template(
            current_domain + "/errors/forbidden_page.html"), 405


    @app.errorhandler(404)
    def page_not_found(error):
        return render_template(
            current_domain + "/errors/page_not_found.html"), 404


    @app.errorhandler(500)
    def forbidden_page(error):
        return render_template(
            current_domain + "/errors/server_error.html"), 500

    @app.errorhandler(501)
    def forbidden_page(error):
        return render_template(
            current_domain + "/errors/server_error.html"), 501


