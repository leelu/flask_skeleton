__author__ = 'leela'
from flask_script import Manager
from app_code import create_app
"""Manager is an instance created out of Flask-Script, which runs Flask instance from commandline"""
app = create_app()
manager = Manager(app)

if __name__ == "__main__":
    manager.run()

