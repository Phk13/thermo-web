from thermo.app import app
from thermo.server import server    # Import for gunicorn

if __name__ == '__main__':
    app.run_server(debug=True)
