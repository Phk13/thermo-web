import dash


app = dash.Dash(__name__, url_base_pathname='/thermo/', update_title=None)
server = app.server
