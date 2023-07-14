from flask import request, render_template, redirect
from models.new import New
from aengine_flask.screen import Screen
from helpers import get_user


class AccountScreen(Screen):
    def main(self):
        user = get_user(request)
        if user:
            query = New.query.all()
            ids = [i.owner_id for i in query]
            return render_template("account.html", data=query, user=user, ids=ids)
        return redirect("/login")
