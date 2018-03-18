from flask import Blueprint
from flask import render_template


views_bp = Blueprint('conntestd_views', __name__)


@views_bp.route('/')
def dashboard():
    return render_template('dashboard.html')
