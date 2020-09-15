from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from config import Config
from serve.database import db
from serve.views.acceptance import acceptance_router
from serve.views.patient import patient_router


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(acceptance_router, url_prefix="/api")
    app.register_blueprint(patient_router, url_prefix="/api")

    return app


app = create_app()
