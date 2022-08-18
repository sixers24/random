from pyBC.datagetter.loader import get_prices_df
from pyBC.analytics.corr import CorrClient
import dash
from dash import Dash, dcc, html, dash_table 
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import dash_core_components as dcc
import plotly.express as px
from datetime import date 
import pandas as pd

app = dash.Dash()

df = get_prices_df()



app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'Equity Mkt Correlation', style = {'textAlign':'center',\
                                            'marginTop':40,'marginBottom':40}),

        dcc.Dropdown( id = 'dropdown',
                        options = [
                            {'label':'pearson_corr', 'value':'pearson' },
                            {'label': 'ols', 'value':'ols'},
                            {'label': 'weird', 'value':'weird'},
                            ],
                        value = 'pearson'),
        html.H2("inital window"),
        dcc.DatePickerRange(
                id='date-picker-range',
                minimum_nights=2,
                min_date_allowed=date(2010, 1, 1),
                max_date_allowed=pd.Timestamp('now').date(),
                start_date_placeholder_text=date(2010, 1, 1),
                end_date=pd.Timestamp('now').date()
                ),
        dash_table.DataTable(#df.to_dict('records'), 
                           # [{"name": i, "id": i} for i in df.columns],
                            id='topten_val'),
       
        html.H2("Trade Size"),
        dcc.Input(id="trade-size",  type='number', min=2, max=10, step=1, debounce=True),
 

        dcc.Graph(id = 'bar_plot'),
        

    ])


@app.callback(
    Output('topten_val', 'data'),
    Input('date-picker-range', 'start_date'),
    Input('date-picker-range', 'end_date'),
    Input('dropdown', 'value'),
     )
def select_data(start_date, end_date, value):

    sub_df = df[start_date:end_date]

    print(start_date, end_date)
    print(sub_df.index.min(), sub_df.index.max())

    if value == 'pearson':
        s = CorrClient.pearson(sub_df)
    elif value == 'ols':
        s = sub_df
    elif value == 'weird':
        s = sub_df    
    print(s)
    return  s.to_dict('records')

 




if __name__ == '__main__': 
    app.run_server(debug=True)