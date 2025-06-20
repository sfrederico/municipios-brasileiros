from app.controllers.home import HomeController


def register_routes(app):
    app.add_url_rule("/", "index", HomeController.index)
