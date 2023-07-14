from flask import request, render_template, redirect
from models.new import New
from aengine_flask.screen import Screen
from helpers import get_user


class AboutScreen(Screen):
    def main(self):
        user = get_user(request)
        if user:
            return render_template("about.html")
        return redirect("/login")
