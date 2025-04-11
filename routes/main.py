from flask import render_template, request, url_for, redirect, flash, send_file, Blueprint
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy import func, desc, or_, cast, String, not_, literal, text
from models import form
from settings import *

main_bp = Blueprint('model', __name__)

@main_bp.route("/", methods=["GET", "POST"])
@login_required
def route_index():
    pass