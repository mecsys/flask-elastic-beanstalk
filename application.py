from flask import Flask

application = Flask(__name__)

@application.route('/')
def application():
    return 'version 0.0.1'
