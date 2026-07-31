from flask import Flask


def createApp():
    app=Flask(__name__)
    app.config["DEBUG"]=True
    from app.routes.home import home
    from app.routes.weather import weather
    app.register_blueprint(home)
    app.register_blueprint(weather)
    return app




    