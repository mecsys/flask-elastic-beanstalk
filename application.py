from flask import Flask

application = Flask(__name__)

@application.route('/')
def home():
    return 'version 0.0.1'
    