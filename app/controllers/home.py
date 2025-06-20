from flask import render_template


class HomeController:
    @staticmethod
    def index():
        """
        Render the home page.
        """
        return render_template("home.html")
