from hashlib import sha256
from uuid import uuid4

from flask import request, render_template, redirect
from models.user import User
from aengine_flask.screen import Screen
from settings import db


class LoginScreen(Screen):
    options = {
        "methods": ["POST", "GET"]
    }

    def main(self):
        if request.method == "POST":
            form = request.form
            if form:
                name = form.get("name")
                passwd = form.get("password")
                passwd = sha256(passwd.encode("utf-8")).hexdigest()
                user = User.query.filter_by(name=name).first()
                if user and passwd == user.password:
                    answer = redirect("/")
                    ident = uuid4().hex
                    answer.set_cookie("session_id", ident, 3600)
                    user.session_id = ident
                    db.session.commit()
                    return answer
        return render_template("login.html")
