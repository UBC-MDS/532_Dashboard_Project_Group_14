import dash
import pandas as pd
# import dash_core_components as dcc
import dash_html_components as html
import altair as alt

df = pd.read_csv("../data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

chart_monthly_income = alt.Chart(
    df, title='Monthly Income Distribution by Attrition'
    ).mark_boxplot().encode(
    x='MonthlyIncome',
    y='Attrition',
    color='Attrition'
)

app = dash.Dash(__name__)
app.layout = html.Div([
    html.Iframe(
        srcDoc=chart_monthly_income.to_html(),
        style={'border-width': '0', 'width': '100%', 'height': '400px'}
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
