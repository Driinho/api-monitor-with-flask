from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .routes import bp
    from .api import api

    app.register_blueprint(bp)
    app.register_blueprint(api)

    return app