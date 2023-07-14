from flask import request, render_template, redirect
from models.user import User
from aengine_flask.screen import Screen
from settings import db
from hashlib import sha256


class RegisterScreen(Screen):
    options = {
        "methods": ["POST", "GET"]
    }

    def main(self):
        if request.method == "POST":
            form = request.form
            if form:
                if form.get("name") and form.get("password"):
                    name = form.get("name")
                    passwd = form.get("password")
                    passwd = sha256(passwd.encode("utf-8")).hexdigest()
                    user = User.query.filter_by(name=name).first()
                    if user:
                        return redirect("/login")
                    user = User(name=name, password=passwd)
                    db.session.add(user)
                    db.session.commit()
                    return redirect("/login")
        return render_template("register.html")
