from flask import Flask

from app.db import init_db
from app.routes import register_routes
from app.settings import Settings


def create_app():
    app = Flask(__name__, template_folder=Settings.TEMPLATE_FOLDER)

    # Load configuration
    app.config.from_object(Settings)

    # Register routes
    register_routes(app)

    # Initialize database
    init_db(app)

    return app


app = create_app()

if __name__ == "__main__":
    app.run()
