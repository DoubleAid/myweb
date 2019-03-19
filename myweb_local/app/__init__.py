from flask import Flask,render_template
from app.Views import config_blueprint

def config_errorhandler(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error/404.html',e=e)

def create_app():
    app = Flask(__name__)
    config_blueprint(app)
    config_errorhandler(app)
    return app


