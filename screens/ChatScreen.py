from uuid import uuid4

from flask import request, render_template, redirect
from models.message import Message
from aengine_flask.screen import Screen
from helpers import get_user
from settings import db


class ChatScreen(Screen):
    options = {
        "methods": ["POST", "GET"]
    }

    def main(self):
        user = get_user(request)
        if request.method == "POST":
            form = request.form
            if form:
                message = form.get('message')
                if message != "":
                    m = Message(id=uuid4().hex, from_id=user.id, text=message)
                    db.session.add(m)
                    db.session.commit()
                    return redirect("/chat")
        if user:
            return render_template("chat.html", data=Message.query.all(), user=user)
        return redirect("/login")
