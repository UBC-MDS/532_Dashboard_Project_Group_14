import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import altair as alt
from dash.dependencies import Input, Output

df = pd.read_csv("../data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
app.layout = html.Div([
    html.Iframe(
        id='m_income_plt',
        style={'border-width': '0', 'width': '100%', 'height': '150px'}
    ),
    'Select a monthly income range to view the attrition distribution',
    dcc.RangeSlider(
        id='income_slider',
        min=0,
        max=df['MonthlyIncome'].max(),
        value=[2000, 18000],
        step=500,
        marks={5000: '$5,000', 10000: '$10,000', 15000: '$15,000'},
        tooltip={'always_visible': True, 'placement': 'bottomLeft'}
    )
])

@app.callback(
    Output('m_income_plt', 'srcDoc'),
    Input('income_slider', 'value'))
def plot_altair(xmax=0):
    chart_monthly_income = alt.Chart(
        df[(df['MonthlyIncome'] >= xmax[0]) & (df['MonthlyIncome'] <= xmax[1])], 
        title='Monthly Income Distribution by Attrition'
        ).mark_boxplot().encode(
        alt.X('MonthlyIncome', scale=alt.Scale(zero=False)),
        y='Attrition',
        color='Attrition')
    return chart_monthly_income.to_html()


if __name__ == '__main__':
    app.run_server(debug=True)
