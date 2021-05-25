from thermo.server import app
from thermo.layout import thermo_layout
import thermo.callback                      # Callback imports for layout


app.title = "Thermo"
app.layout = thermo_layout()

