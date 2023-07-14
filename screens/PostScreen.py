from flask import request, render_template, redirect
from models.new import New
from aengine_flask.screen import Screen
from helpers import get_user
from settings import db, base_dir


class PostScreen(Screen):
    options = {
        "methods": ["POST", "GET"]
    }

    def main(self):
        user = get_user(request)
        if request.method == "POST":
            if request.form:
                form = request.form
                if request.files:
                    file = request.files["photo"]
                else:
                    file = None
                if file:
                    path = f"{base_dir}/static/imgs/upload/{file.filename}"
                    save_path = f"/static/imgs/upload/{file.filename}"

                else:
                    path = ""
                new = New(owner_id=user.id, text=form.get("message"), image_uri=save_path)
                file.save(path)
                db.session.add(new)
                db.session.commit()
                return redirect("/account")

        if user:
            return render_template("publish.html")
        return redirect("/login")
