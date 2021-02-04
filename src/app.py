from altair.vegalite.v4.schema.channels import Opacity
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import altair as alt
import pandas as pd
import dash_bootstrap_components as dbc

# Read Data - Don't Change the Path
df = pd.read_csv(r"data/Processed/HR_employee_Attrition_editted.csv")
# Convert variables to categoriccal and reordering by label.
df['EnvironmentSatisfaction'] = df['EnvironmentSatisfaction'].astype('category').cat.rename_categories(["1 - Bad", "2 - Good", "3 - Better", "4 - Best"])
df['WorkLifeBalance']=df['WorkLifeBalance'].astype('category').cat.rename_categories(["1 - Low", "2 - Medium", "3 - High", "4 - Very High"])
df["Department"]=df["Department"].astype('category')
df["BusinessTravel"]=df["BusinessTravel"].astype('category')
df['BusinessTravel'] = df['BusinessTravel'].cat.rename_categories(["1 - No Travel", "3 - Travel Frequently", "2 - Travel Rarely"])

# Setup app and layout/frontend
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

def plot_summaries(df=df):

    chart_att_department = alt.Chart(
        df, 
        title='Attrition by Department').mark_bar(size=60, opacity= 0.8).encode(
        x=alt.X('Department', title='', axis=alt.Axis(grid=False, labelAngle=10)), #scale=alt.Scale(domain=["Low", "Medium", "High", "Very High"])
        y=alt.Y('count()', stack = 'normalize', axis=alt.Axis(format='%', grid=False), title = 'Proportion'),
        color =alt.Color('Attrition', scale=alt.Scale(range=["#00BFC4", "#F8766D"])),
        ).properties(height=200, width=250)

    chart_att_gender = alt.Chart(
        df, 
        title='Attrition by Department').mark_bar(size=70, opacity= 0.8).encode(
        x=alt.X('Gender', title='', axis=alt.Axis(grid=False,labelAngle=10)), #scale=alt.Scale(domain=["Low", "Medium", "High", "Very High"])
        y=alt.Y('count()', stack = 'normalize', axis=alt.Axis(format='%', grid=False), title = 'Proportion'),
        color = 'Attrition'
        ).properties(height=200, width=250)

    chart = (chart_att_department | chart_att_gender) 

    return chart.to_html()



app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('Key Factors for Employee Attrition Dashboard', 
            style={
                    'color' : 'b', 
                    'background-color' : '#f0f0f1', 
                    'textAlign': 'center',
                    'justify': "center",
                    'font-size': '48px',
                    'font-family': 'Roboto'
                   }),
            html.Br(),
        ], style={'backgroundColor': '#f0f0f1',
                    'border-radius': 3,
                    'padding': 5,
                    #'margin-top': 20,
                    'margin-bottom': 15,
                    'margin-right': 15
        })                  
    ]),
    dbc.Row([
        dbc.Col([
            dbc.CardHeader('Attrition Overview', 
                    style={
                    'textAlign': 'center',
                    'justify': "center",
                    'font-size': '24px',
                    'font-family': 'Proxima Nova' #Roboto, Open Sans, 
                   }),
                dbc.CardBody(
                    html.Iframe(
                        id='summary_plots',
                        srcDoc=plot_summaries(),
                        style={'justify': "center",
                                'border-width': '0', 
                                'width': '200%', 
                                'height': '300px'}
                                ),style={
                                    'textAlign': 'right',
                                    'justify': "center",
                                    'font-size': '24px',
                                    'font-family': 'Roboto'}
                            )
        ])]),

    dbc.Row([
        dbc.Col([
            'Department',
            dcc.Dropdown(
                id='depart-widget',
                value=['Sales', 'Human Resources', 'Research & Development'],
                options=[
                    {'label': col, 'value': col} for col in list(set(df.Department.tolist()))],
                multi=True,
                placeholder='Select a department'),
            
            'Gender',
            dcc.Dropdown(
                id='gender-widget',
                value=['Female', 'Male'],  # REQUIRED to show the plot on the first page load
                options=[
                    {'label': "Female", 'value': "Female"},
                    {'label': "Male", 'value': "Male"}],
                multi=True,
                placeholder='Select gender'
                ),

            'Age',
            dcc.RangeSlider(
                id='age_slider',
                min=df['Age'].min(),
                max=df['Age'].max(),
                value=[18, 60],
                step=1,
                marks={30: '30', 40: '40', 50:'50'},
                tooltip={'always_visible': True, 'placement': 'bottomLeft'})],
            md=4,),
          
        dbc.Col(
            html.Iframe(
                id='scatter',
                style={'border-width': '0', 'width': '200%', 'height': '1000px'}),
                )]),

]) 
# Set up callbacks/backend
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('depart-widget', 'value'),
    Input('gender-widget', 'value'),
    Input('age_slider', 'value'))

def plot_altair(depart,gender, age=18):
    # filter data based on criteria
    data = df[(df['Department'].isin(depart)) & (df['Gender'].isin(gender))&(df['Age']>=age[0])&(df['Age']<=age[1])]

    col_range = ["#00BFC4", "#F8766D"]
    # distribution on monthly income

    chart_income = alt.Chart(data, title='Monthly Income Distribution').mark_boxplot(size = 50).encode(
        x=alt.X('MonthlyIncome:Q', scale=alt.Scale(zero=False), axis=alt.Axis(grid=False)),
        y=alt.Y('Attrition',  axis=alt.Axis(grid=False)),
        color=alt.Color('Attrition', scale=alt.Scale(range=col_range)) 
        #scale=alt.Scale(domain=domain, range=range_) scheme='tableau20'
        ).properties(height=200, width=250)
    
    chart_worklife = alt.Chart(
        data, 
        title='Work Life Balance').mark_bar(opacity= 0.8).encode(
        y=alt.Y('WorkLifeBalance:O', title='', axis=alt.Axis(grid=False)), #scale=alt.Scale(domain=["Low", "Medium", "High", "Very High"])
        x=alt.X('count()', stack = 'normalize', axis=alt.Axis(format='%', grid=False), title = 'Proportion'),
        color = 'Attrition'
    ).properties(height=200, width=250)
    
    chart_travel = alt.Chart(
        data,
        title='Business Travel Frequency').mark_bar(opacity= 0.8).encode(
        y=alt.Y("BusinessTravel", title="", axis=alt.Axis(grid=False)),
        x=alt.X('count()', stack="normalize", axis=alt.Axis(format='%', grid=False), title='Proportion'),
        color = "Attrition").properties(height=200, width=250)
    
    chart_environment = alt.Chart(
        data, 
        title='Environment Satisfaction').mark_bar(opacity= 0.8).encode(
        y=alt.Y('EnvironmentSatisfaction', title='', axis=alt.Axis(grid=False)),
        x=alt.X('count()', stack = 'normalize', axis=alt.Axis(format='%', grid=False), title = 'Proportion'),
        color='Attrition').properties(height=200, width=250)
    
    chart = ((chart_income&chart_travel) | (chart_worklife&chart_environment))
    return chart.to_html()



if __name__ == '__main__':
    app.run_server(debug=True)        #debug=True