from flask import Blueprint, redirect, render_template, request, session, url_for

from temp.forms import LoginForm

main_b = Blueprint("main", __name__)


@main_b.route("/", methods=["GET", "POST"])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        session["name"] = form.name.data
        session["room"] = form.room.data
        return redirect(url_for(".chat"))
    elif request.method == "GET":
        form.name.data = session.get("name", "")
        form.room.data = session.get("room", "")
    return render_template("index.html", form=form)


@main_b.route("/chat")
def chat():
    name = session.get("name", "")
    room = session.get("room", "")
    if name == "" or room == "":
        return redirect(url_for(".index"))
    return render_template("chat.html", name=name, room=room)
