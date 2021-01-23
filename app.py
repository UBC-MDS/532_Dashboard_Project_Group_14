import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import altair as alt
import pandas as pd
import dash_bootstrap_components as dbc

#updated data path
df = pd.read_csv(r"data/Processed/HR_employee_Attrition_editted.csv")
###Convert variables to categoriccal and reordering by label.
df['EnvironmentSatisfaction'] = df['EnvironmentSatisfaction'].astype('category').cat.rename_categories(["Bad", "Good", "Better", "Best"])
df['WorkLifeBalance']=df['WorkLifeBalance'].astype('category').cat.rename_categories(["Low", "Medium", "High", "Very High"])
df["Department"]=df["Department"].astype('category')
df["BusinessTravel"]=df["BusinessTravel"].astype('category')
df['BusinessTravel'] = df['BusinessTravel'].cat.rename_categories(["No Travel", "Travel Frequently", "Travel Rarely"])
#df['BusinessTravel'] = df['BusinessTravel'].cat.reorder_categories(["Travel Rarely", "Travel Frequently", "No Travel"], ordered=True)

# Setup app and layout/frontend
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.layout = dbc.Container([
    html.H1('Key Factors for Employee Attrition'),
    dbc.Row([
        dbc.Col([
            'Department',
            dcc.Dropdown(
                id='depart-widget',
                value='Sales',
                options=[
                    {'label': col, 'value': col} for col in list(set(df.Department.tolist()))],
                placeholder='Select a department'),

            # 'Job Role',
            # dcc.Dropdown(
            #     id='job-widget',
            #     value='Sales Representative',
            #     options=[
            #         {'label': col, 'value': col} for col in set(df.JobRole.tolist())],
            #     placeholder='Select a job role'),
            
            'Gender',
            dcc.Dropdown(
                id='gender-widget',
                value='Female',  # REQUIRED to show the plot on the first page load
                options=[
                    {'label': "Female", 'value': "Female"},
                    {'label': "Male", 'value': "Male"}],
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
                style={'border-width': '0', 'width': '200%', 'height': '800px'}),
                )])])  
            #style={"height": "1000vh"}

# Set up callbacks/backend
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('depart-widget', 'value'),
    #Input('job-widget', 'value'),
    Input('gender-widget', 'value'),
    Input('age_slider', 'value'))

def plot_altair(depart,gender, age=18):
    chart_income = alt.Chart(
        df[(df['Department']==depart) & (df['Gender']==gender)&(df['Age']>=age[0])&(df['Age']<=age[1])], 
        title='Monthly Income Distribution'
        ).mark_boxplot(size = 50).encode(
        x=alt.X('MonthlyIncome:Q', scale=alt.Scale(zero=False), axis=alt.Axis(grid=False)),
        y=alt.Y('Attrition',  axis=alt.Axis(grid=False)),
        color='Attrition').properties(height=200, width=250)
    
    chart_worklife = alt.Chart(
        df[(df['Department']==depart) &(df['Gender']==gender)&(df['Age']>=age[0])&(df['Age']<=age[1])], 
        title='Work Life Balance').mark_bar().encode(
        y=alt.Y('WorkLifeBalance:O', title='', scale=alt.Scale(domain=["Low", "Medium", "High", "Very High"])),
        x=alt.X('count()', stack = 'normalize', axis=alt.Axis(format='%'), title = 'Proportion'),
        color = 'Attrition'
    ).properties(height=200, width=250)
    
    chart_travel = alt.Chart(
        df[(df['Department']==depart) &(df['Gender']==gender)&(df['Age']>=age[0])&(df['Age']<=age[1])], 
        title='Business Travel Frequency').mark_bar().encode(
        y=alt.Y("BusinessTravel", title="", scale=alt.Scale(domain=["No Travel", "Travel Rarely", "Travel Frequently"]),
        x=alt.X('count()', stack="normalize", axis=alt.Axis(format='%'), title='Proportion'),
        color = "Attrition").properties(height=200, width=250))
    
    chart_environment = alt.Chart(
        df[(df['Department']==depart) & (df['Gender']==gender)&(df['Age']>=age[0])&(df['Age']<=age[1])], 
        title='Environment Satisfaction').mark_bar().encode(
        y=alt.Y('EnvironmentSatisfaction', title='', scale=alt.Scale(domain=["Bad", "Good", "Better", "Best"])),
        x=alt.X('count()', stack = 'normalize', axis=alt.Axis(format='%'), title = 'Proportion'),
        color='Attrition').properties(height=200, width=250)
    
    chart = (chart_income&chart_travel)|(chart_worklife&chart_environment)
    return chart.to_html()



if __name__ == '__main__':
    app.run_server(debug=True)