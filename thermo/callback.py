from thermo.app import app
from dash.dependencies import Output, Input
from thermo.data import find_date_reading, get_live_reading
from datetime import datetime


@app.callback(
    [Output('last-temp', 'children'), Output('last-hum', 'children'), Output('last-press', 'children'),
     Output('reading-status', 'style')],
    Input('interval-component', 'n_intervals'))
def update_last_read(n):
    reading = get_live_reading()
    if reading is not None:
        return f"{reading.json()['temperature']}ºC", f"{reading.json()['humidity']}%", \
               f"{reading.json()['pressure']} hPa", {'display': 'none'}
    return '0.00ºC', '0.00%', '0.00 hPA', {'display': 'block'}


@app.callback(
    [Output("temperature-chart", "figure"), Output("humidity-chart", "figure"), Output("pressure-chart", "figure"),
     Output("date-range", "max_date_allowed")],
    [Input("date-range", "start_date"), Input("date-range", "end_date")],
)
def update_charts(start_date, end_date):
    data = find_date_reading(start_date, end_date)

    temperature_chart_figure = {
        "data": [
            {
                "x": data["timestamp"],
                "y": data["temperature"],
                "type": "lines",
                "hovertemplate": "%{y:.2f}ºC<extra></extra>",
            },
        ],
        "layout": {
            "title": {"text": "<b>Temperature</b>", "font": {"color": "#FF6839"}},
            "yaxis": {"ticksuffix": "ºC", "fixedrange": True},
            "colorway": ["#62B1F6"],
        },
    }

    humidity_chart_figure = {
        "data": [
            {
                "x": data["timestamp"],
                "y": data["humidity"],
                "type": "lines",
                "hovertemplate": "%{y:.2f}%<extra></extra>",
            },
        ],
        "layout": {
            "title": {"text": "<b>Humidity</b>", "font": {"color": "#FF6839"}},
            "yaxis": {"ticksuffix": "%", "fixedrange": True},
            "colorway": ["#62B1F6"],
        },
    }
    pressure_chart_figure = {
        "data": [
            {
                "x": data["timestamp"],
                "y": data["pressure"],
                "type": "lines",
                "hovertemplate": "%{y:.2f} hPa<extra></extra>",
            },
        ],
        "layout": {
            "title": {"text": "<b>Pressure</b>", "font": {"color": "#FF6839"}},
            "yaxis": {"ticksuffix": "hPa", "fixedrange": True},
            "colorway": ["#62B1F6"],
        },
    }
    return temperature_chart_figure, humidity_chart_figure, pressure_chart_figure, datetime.now()
