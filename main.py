import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.graph_objects import Layout
import pandas as pd
import numpy as np
app = dash.Dash(__name__)

layout = Layout(plot_bgcolor='red')

labels = ["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"]
parents = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"]

fig2 = make_subplots(
   cols = 4, rows = 2,
   column_widths = [1, 1, 1, 1],
   subplot_titles = ('branchvalues', '<b> branchvalues', 
                     'branchvalues','branchvalues: <b>remainder<br />&nbsp;<br />'),

   specs = [[{'type': 'treemap', 'rowspan': 1}, {'type': 'treemap','rowspan': 1}, {'type': 'treemap'}, {'type': 'treemap'}], [{'type': 'treemap', 'rowspan': 1}, {'type': 'treemap','rowspan': 1}, {'type': 'treemap'}, {'type': 'treemap'}]],
   horizontal_spacing = 0.005,
   vertical_spacing = 0.02,
)

fig2.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'paper_bgcolor': 'rgba(0,0,0,0)'
})

fig2.add_trace(go.Treemap(
    labels = labels,
    parents = parents,
   #  values =  [10, 14, 12, 10, 2, 6, 6, 1, 4],
   #  textinfo = "label+value+percent parent+percent entry+percent root",
    root_color="lightgrey",
),row = 1, col = 1)

fig2.add_trace(go.Treemap(
    branchvalues = "total",
    labels = labels,
    parents = parents,
    values = [65, 14, 12, 10, 2, 6, 6, 1, 4],
    textinfo = "label+value+percent parent+percent entry",
    root_color="lightgrey"
),row = 1, col = 2)

fig2.add_trace(go.Treemap(
    branchvalues = "total",
    labels = labels,
    parents = parents,
    values = [65, 14, 12, 10, 2, 6, 6, 1, 4],
    textinfo = "label+value+percent parent+percent entry",
    root_color="lightgrey"
),row = 1, col = 3)

fig2.add_trace(go.Treemap(
    labels = labels,
    parents = parents,
    values =  [10, 14, 12, 10, 2, 6, 6, 1, 4],
    textinfo = "label+value+percent parent+percent entry+percent root",
    root_color="lightgrey"
),row = 1, col = 4)

fig2.add_trace(go.Treemap(
    labels = labels,
    parents = parents,
    values =  [10, 14, 12, 10, 2, 6, 6, 1, 4],
    textinfo = "label+value+percent parent+percent entry+percent root",
    root_color="lightgrey"
),row = 2, col = 1)

app.layout = html.Div(style = {'backgroundColor':'black'},children=[

   html.H1('Stock Market Summary', style = {'color':'white'}),
   html.Div('''
   AI predictions, intraday market price action, biggest movers, sectors performance, and more.
   ''', style = {'color':'white'}),

   dcc.Graph(
      id='example-graph',
      figure=fig2,
   )

]) 
if __name__ == '__main__':
   app.run_server(port = '4050',debug=True)

