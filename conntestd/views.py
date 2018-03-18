from flask import Blueprint
from flask import render_template
from flask import g
from sqlalchemy import desc
from conntestd.db import SpeedTestResult


views_bp = Blueprint('conntestd_views', __name__)


@views_bp.route('/')
def dashboard():
    recent_tests = g.db.query(SpeedTestResult). \
        order_by(desc(SpeedTestResult.dt)).limit(5).all()

    return render_template('dashboard.html',
                           recent_tests=recent_tests)
