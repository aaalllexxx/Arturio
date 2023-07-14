from flask import request, render_template, redirect
from models.new import New
from aengine_flask.screen import Screen
from helpers import get_user


class HomeScreen(Screen):
    def main(self):
        if get_user(request):
            return render_template("index.html", data=New.query.all())
        return redirect("/login")
