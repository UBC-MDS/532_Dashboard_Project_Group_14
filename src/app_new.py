# from altair.vegalite.v4.schema.channels import Opacity
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
df["EnvironmentSatisfaction"] = (
    df["EnvironmentSatisfaction"]
    .astype("category")
    .cat.rename_categories(["1 - Bad", "2 - Good", "3 - Better", "4 - Best"])
)
df["WorkLifeBalance"] = (
    df["WorkLifeBalance"]
    .astype("category")
    .cat.rename_categories(["1 - Low", "2 - Medium", "3 - High", "4 - Very High"])
)
df["Department"] = df["Department"].astype("category")
df["BusinessTravel"] = df["BusinessTravel"].astype("category")
df["BusinessTravel"] = df["BusinessTravel"].cat.rename_categories(
    ["1 - No Travel", "3 - Travel Frequently", "2 - Travel Rarely"]
)


def get_attrition(df):
    """To get attrition rate for given any filtered dataset"""
    attrition_rate = df["Attrition"].value_counts(normalize=True)[1]
    return attrition_rate


df_f = df[df["Gender"] == "Female"]
df_m = df[df["Gender"] == "Male"]
df_hr = df[df["Department"] == "Human Resources"]
df_rd = df[df["Department"] == "Research & Development"]
df_s = df[df["Department"] == "Sales"]


# Setup app and layout/frontend
app = dash.Dash(
    __name__,
    title="Employee Attrition Dashboard",
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)
server = app.server

# Setup sidebar style
SIDEBAR_STYLE = {
    # "position": "fixed",
    #"top": 360,
    # "left": 50,
    # "bottom": 10,
    "justify": "center",
    "width": "20rem",
    "padding": "3rem 1rem",
    "background-color": "#D4E6F1", 
}
# Setup the main content style
CONTENT_STYLE = {
    #"position": "center",   # "position": "fixed",
    # "top": 56.5,
    # "left": 360,
    # "bottom": 10,
    # 'right': 20,
    "width": "66rem",
    "padding": "3rem 1rem",
    # "margin-left": "12rem",
    # "margin-right": "rem",
    # "padding": "2rem 1rem",
    "background-color": "#f0f0f1",
}

# set up summary plots
# def plot_summaries(df=df):

#     chart_att_department = alt.Chart(
#         df,
#         title='Attrition by Department').mark_bar(size=60, opacity= 0.8).encode(
#         x=alt.X('Department', title='', axis=alt.Axis(grid=False, labelAngle=10)), #scale=alt.Scale(domain=["Low", "Medium", "High", "Very High"])
#         y=alt.Y('count()', stack = 'normalize', axis=alt.Axis(format='%', grid=False), title = 'Proportion'),
#         color=alt.Color('Attrition', scale=alt.Scale(range=["#00BFC4", "#F8766D"])),
#         #tooltip='Attrition'
#         ).properties(height=200, width=250)

#     chart_att_gender = alt.Chart(
#         df,
#         title='Attrition by Gender').mark_bar(size=70, opacity= 0.8).encode(
#         x=alt.X('Gender', title='', axis=alt.Axis(grid=False,labelAngle=10)), #scale=alt.Scale(domain=["Low", "Medium", "High", "Very High"])
#         y=alt.Y('count()', stack = 'normalize', axis=alt.Axis(format='%', grid=False), title = 'Proportion'),
#         color = alt.Color('Attrition', scale=alt.Scale(range=["#00BFC4", "#F8766D"])),
#         # tooltip='female_attrition_rate'
#         ).properties(height=200, width=250)

#     chart = (chart_att_department | chart_att_gender)

#     return chart_att_department.to_html(), chart_att_gender.to_html() #chart.to_html()

# Define cards for the dashboard
cards = [
    dbc.Card(
        [
            dbc.CardHeader("Overall"),
            dbc.CardBody(
                [html.H4(f"{get_attrition(df)*100:.2f}%", className="card-title"),],
                style={"font-size": 15},
            ),
        ],
        color="light",
        style={"font-size": 14},
    ),
    dbc.Card(
        [
            dbc.CardHeader("By Gender"),
            dbc.CardBody(
                [
                    html.H4(f"{get_attrition(df_f)*100:.2f}%", className="card-title"),
                    html.P("Female", className="card-text"),
                    html.H4(f"{get_attrition(df_m)*100:.2f}%", className="card-title"),
                    html.P("Male", className="card-text"),
                ],
                style={"font-size": 15},
            ),
        ],
        color="light",
        style={"font-size": 14},
    ),
    # dbc.Card(
    #     [
    #         html.H2(f"{get_attrition(df_f)*100:.2f}%", className="card-title"),
    #         html.P("Female", className="card-text"),
    #         html.H2(f"{get_attrition(df_m)*100:.2f}%", className="card-title"),
    #         html.P("Male", className="card-text"),
    #      ],
    #     body=True,
    #     color="light",
    # ),
    dbc.Card(
        [
            dbc.CardHeader("By Department"),
            dbc.CardBody(
                [
                    html.H4(f"{get_attrition(df_hr)*100:.2f}%", className="card-title"),
                    html.P("Human Resources", className="card-text"),
                    html.H4(f"{get_attrition(df_rd)*100:.2f}%", className="card-title"),
                    html.P("Research & Development", className="card-text"),
                    html.H4(f"{get_attrition(df_s)*100:.2f}%", className="card-title"),
                    html.P("Sales", className="card-text"),
                ],
                style={"font-size": 15},
            ),
        ],
        color="light",
        style={"font-size": 14},
    ),
]

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1(
                            "Employee Attrition Dashboard",
                            style={
                                "background-color": "#f0f0f1",
                                "textAlign": "center",
                                "justify": "center",
                                "margin-top": 20,
                                "margin-bottom": 0,
                                "font-size": "40px",
                                #"font-family": "Lato",
                            },
                        ),
                        html.Br(),
                    ],
                    style={
                        "backgroundColor": "#f0f0f1",
                        "padding": 5,
                        "margin-top": 20,
                        "margin-bottom": 5,
                        "margin-right": 30,
                    },
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.H2("Dashboard Filters for Key Factors", className="display-10"),
                        html.Hr(),
                        html.Br(),
                        dcc.Markdown("""_Department_"""),
                        dcc.Dropdown(
                            id="depart-widget",
                            value=[
                                "Sales",
                                "Human Resources",
                                "Research & Development",
                            ],
                            options=[
                                {"label": col, "value": col}
                                for col in list(set(df.Department.tolist()))
                            ],
                            multi=True,
                            placeholder="Select a department",
                        ),
                        html.Br(),
                        dcc.Markdown("""_Gender_"""),
                        dcc.Dropdown(
                            id="gender-widget",
                            value=[
                                "Female",
                                "Male",
                            ],  # REQUIRED to show the plot on the first page load
                            options=[
                                {"label": "Female", "value": "Female"},
                                {"label": "Male", "value": "Male"},
                            ],
                            multi=True,
                            placeholder="Select gender",
                        ),
                        html.Br(),
                        dcc.Markdown("""_Age_"""),
                        dcc.RangeSlider(
                            id="age_slider",
                            min=df["Age"].min(),
                            max=df["Age"].max(),
                            value=[18, 60],
                            step=1,
                            marks={30: "30", 40: "40", 50: "50"},
                            tooltip={"always_visible": False, "placement": "bottom"},
                        ),
                    ],
                    style=SIDEBAR_STYLE,
                    width="auto",
                ),
                dbc.Col(
                    [
                        dbc.Col(
                            [
                                dbc.Row(
                                    dbc.Col(
                                        dbc.CardHeader(
                                            "Attrition Rate Overview",
                                            style={
                                                "textAlign": "center",
                                                "justify": "center",
                                                "font-size": "20px",
                                                "border-radius": 3,
                                                "backgroundColor": "#f0f0f1",
                                            },
                                        ),
                                    )
                                ),
                                dbc.Row(
                                    [dbc.Col(card) for card in cards], no_gutters=True,
                                ),
                                dbc.Row(
                                    dbc.Col(
                                        dbc.CardHeader(
                                            "Key Factors for Employee Attrition",
                                            style={
                                                "textAlign": "center",
                                                "justify": "center",
                                                "font-size": "20px",
                                                "border-radius": 3,
                                                "backgroundColor": "#f0f0f1",
                                            },
                                        ),
                                    )
                                ),
                            ],
                        ),
                        html.Br(),
                        html.Iframe(
                            id="scatter",
                            style={
                                "border-width": "0",
                                "width": "200%",
                                "height": "550px",
                                "horizontalAlign": "center",
                                },
                        
                        ),
                    ]
                ),
            ]
        ),
    ]
)


# Set up callbacks/backend
@app.callback(
    Output("scatter", "srcDoc"),
    Input("depart-widget", "value"),
    Input("gender-widget", "value"),
    Input("age_slider", "value"),
)
def plot_altair(depart, gender, age=18):
    """
    Taking in values from dropdowns and sliders to 
    to plot four main charts for "key factors for employee attrition" section

    Parameters
    ----------
    deparment : str
        the selected department from drop down, can be multiple values
    gender : str 
        the selected department from drop down, can be multiple values
    age : list
        the range of age to be filtered with min and max value

    Returns
    -------
    html
        The html charts to show in the dashboard 
    """

    #"""Plot four main charts - key factors for employee attrition"""
    # filter data based on criteria
    data = df[
        (df["Department"].isin(depart))
        & (df["Gender"].isin(gender))
        & (df["Age"] >= age[0])
        & (df["Age"] <= age[1])
    ]

    col_range = ["#00BFC4", "#F8766D"]
    # distribution on monthly income

    chart_income = (
        alt.Chart(data, title="Monthly Income Distribution")
        .mark_boxplot(size=50, color="Attrition")
        .encode(
            x=alt.X(
                "MonthlyIncome:Q",
                title="Month Income (in thousands)",
                scale=alt.Scale(zero=False),
                axis=alt.Axis(grid=False, format="$~s"),
            ),
            y=alt.Y("Attrition", axis=alt.Axis(grid=False, title="")),
            color=alt.Color("Attrition", scale=alt.Scale(range=col_range))
            # scale=alt.Scale(domain=domain, range=range_) scheme='tableau20'
        )
        .properties(height=200, width=250)
    )

    chart_worklife = (
        alt.Chart(data, title="Work Life Balance")
        .mark_bar(opacity=0.8)
        .encode(
            y=alt.Y(
                "WorkLifeBalance:O", title="", axis=alt.Axis(grid=False)
            ),  # scale=alt.Scale(domain=["Low", "Medium", "High", "Very High"])
            x=alt.X(
                "count()",
                stack="normalize",
                axis=alt.Axis(format="%", grid=False),
                title="Proportion",
            ),
            color="Attrition",
        )
        .properties(height=200, width=250)
    )

    chart_travel = (
        alt.Chart(data, title="Business Travel Frequency")
        .mark_bar(opacity=0.8)
        .encode(
            y=alt.Y("BusinessTravel", title="", axis=alt.Axis(grid=False)),
            x=alt.X(
                "count()",
                stack="normalize",
                axis=alt.Axis(format="%", grid=False),
                title="Proportion",
            ),
            color="Attrition",
        )
        .properties(height=200, width=250)
    )

    chart_environment = (
        alt.Chart(data, title="Environment Satisfaction")
        .mark_bar(opacity=0.8)
        .encode(
            y=alt.Y("EnvironmentSatisfaction", title="", axis=alt.Axis(grid=False)),
            x=alt.X(
                "count()",
                stack="normalize",
                axis=alt.Axis(format="%", grid=False),
                title="Proportion",
            ),
            color="Attrition",
        )
        .properties(height=200, width=250)
    )

    chart = (chart_income & chart_travel) | (chart_worklife & chart_environment)
    return chart.to_html()


if __name__ == "__main__":
    app.run_server(debug=True, host="127.0.0.1")  # debug=True, host="127.0.0.1"
