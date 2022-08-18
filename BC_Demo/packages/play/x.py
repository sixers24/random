import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, html, dcc, dash_table, callback
#step 2
app = Dash(__name__)
#step 3
app.layout = html.Div([ 
         html.H1("Bootstrap Grid System Example")
         , dbc.Row(dbc.Col(html.Div(dbc.Alert("This is one column", color= "primary")))
                   )#end row 1
         , dbc.Row([
              dbc.Col(html.Div(dbc.Alert("One of three columns", color= "primary")))
              , dbc.Col(html.Div(dbc.Alert("One of three columns", color= "primary")))
              , dbc.Col(html.Div(dbc.Alert("One of three columns", color= "primary")))
              ]) #end row 2
         ]) #end div
#step 4
if __name__ == "__main__":
     app.run_server(debug = True)