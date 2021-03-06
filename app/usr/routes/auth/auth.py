from ... import usr
from flask import render_template
from ...form.forms import LoginForm


@usr.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)