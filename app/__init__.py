from flask import Flask

def create_app():
    app = Flask(__name__)

    # 加載配置
    app.config.from_object('config.Config')

    # 註冊 Blueprint
    from .routes import main
    app.register_blueprint(main)

    return app
