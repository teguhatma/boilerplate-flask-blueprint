from flask import Blueprint

usr = Blueprint("usr", __name__, template_folder="templates")

from .routes import home