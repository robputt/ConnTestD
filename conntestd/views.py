import pygal
import datetime
from flask import Blueprint
from flask import render_template
from flask import g
from sqlalchemy import desc
from sqlalchemy import asc
from pygal.style import CleanStyle
from conntestd.db import SpeedTestResult


views_bp = Blueprint('conntestd_views', __name__)


def seven_day_speed_graph():
    line_chart = pygal.Line(x_label_rotation=20,
                            legend_at_bottom=True,
                            style=CleanStyle,
                            x_labels_major_every=100,
                            show_minor_x_labels=False)
    line_chart.title = 'Download / Upload Speeds'

    now = datetime.datetime.now()
    week_ago = now - datetime.timedelta(weeks=1)
    week_results = g.db.query(SpeedTestResult). \
        filter(SpeedTestResult.dt > week_ago). \
        filter(SpeedTestResult.status == 'complete'). \
        order_by(asc(SpeedTestResult.dt)).all()

    dt_list = []
    d_list = []
    u_list = []
    for result in week_results:
        dt_list.append(result.dt)
        d_list.append(result.download / 1024 / 1024)
        u_list.append(result.upload / 1024 / 1024)

    line_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d %H:%M'), dt_list)
    line_chart.add("Download (Mbit/s) ", d_list)
    line_chart.add("Upload (Mbit/s)", u_list)
    return line_chart.render_data_uri()


def seven_day_ping_graph():
    line_chart = pygal.Line(x_label_rotation=20,
                            legend_at_bottom=True,
                            style=CleanStyle,
                            x_labels_major_every=100,
                            show_minor_x_labels=False)
    line_chart.title = 'Ping'

    now = datetime.datetime.now()
    week_ago = now - datetime.timedelta(weeks=1)
    week_results = g.db.query(SpeedTestResult). \
        filter(SpeedTestResult.dt > week_ago). \
        filter(SpeedTestResult.status == 'complete'). \
        order_by(asc(SpeedTestResult.dt)).all()

    dt_list = []
    p_list = []
    for result in week_results:
        dt_list.append(result.dt)
        p_list.append(result.ping)

    line_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d %H:%M'), dt_list)
    line_chart.add("Ping (ms) ", p_list)
    return line_chart.render_data_uri()

@views_bp.route('/')
def dashboard():
    recent_tests = g.db.query(SpeedTestResult). \
        order_by(desc(SpeedTestResult.dt)).limit(5).all()

    speed_graph = seven_day_speed_graph()
    ping_graph = seven_day_ping_graph()

    return render_template('dashboard.html',
                           recent_tests=recent_tests,
                           speed_graph=speed_graph,
                           ping_graph=ping_graph)
