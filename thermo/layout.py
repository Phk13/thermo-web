import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime, timedelta
from thermo.app import app
from config import SENSOR_INTERVAL


def thermo_layout():
    return html.Div(
        children=[
            html.Img(src=app.get_asset_url('error.png'), className="header-reading-status", id='reading-status'),
            html.Div(
                children=[
                    html.Img(src=app.get_asset_url('thermo.png'), className="header-logo"),
                    html.H1(children="Thermo",
                            className="header-title",
                            ),
                    html.Div(children=[
                        html.Div(children=[
                            html.Img(src=app.get_asset_url('temperature.png'), className="header-reading-icon"),
                            html.Div(children='0.00ºC', className="header-reading-value", id="last-temp"),
                        ], className="header-reading-block"),
                        html.Div(children=[
                            html.Img(src=app.get_asset_url('humidity.png'), className="header-reading-icon"),
                            html.Div(children='0.00%', className="header-reading-value", id="last-hum"),
                        ], className="header-reading-block"),
                        html.Div(children=[
                            html.Img(src=app.get_asset_url('pressure.png'), className="header-reading-icon"),
                            html.Div(children='0.00 hPa', className="header-reading-value", id="last-press"),
                        ], className="header-reading-block"),
                        dcc.Interval(
                            id='interval-component',
                            interval=SENSOR_INTERVAL,
                            n_intervals=0
                        )
                    ], className="header-reading-wrapper"),
                ],
                className="header"
            ),
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.Div(children="Date Range", className="menu-title"),
                            dcc.DatePickerRange(
                                id="date-range",
                                display_format='YYYY/MM/DD',
                                first_day_of_week=1,
                                min_date_allowed="2021-03-01",
                                max_date_allowed=datetime.now(),
                                start_date=datetime.now().replace(hour=0, minute=0, second=0) - timedelta(days=7),
                                end_date=datetime.now().replace(hour=23, minute=59, second=59),
                                persistence=True,
                                persisted_props=['start_date', 'end_date'],
                            ),
                        ]
                    ),
                ], className="menu",
            ),
            html.Div(
                children=[
                    html.Div(children=dcc.Graph(id="temperature-chart"), className="card"),
                    html.Div(children=dcc.Graph(id="humidity-chart"), className="card"),
                    html.Div(children=dcc.Graph(id="pressure-chart"), className="card"),
                ], className="wrapper",
            ),
        ]
    )
