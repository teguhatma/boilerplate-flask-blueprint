from .. import admin
from flask import render_template


@admin.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", title="Dashboard")