from ... import usr
from flask import render_template, redirect, url_for, flash, request
from ...form.forms import LoginForm
from flask_login import login_user, login_required, current_user, logout_user
from app.models import User


@usr.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("admin.dashboard"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            next = request.args.get("next")
            if next is None or not next.startswith("/"):
                if user:
                    next = url_for("admin.dashboard")
            return redirect(next)
        elif user is None:
            flash("Maaf, Anda belum terdaftar.", "info")
        else:
            flash("Email dan password anda salah.", "info")
    return render_template("login.html", title="Login", form=form)


@usr.route("/logout")
def logout():
    logout_user()
    return redirect(url_for(".login"))
