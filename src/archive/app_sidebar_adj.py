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
attrition_rate = df["Attrition"].value_counts(normalize=True)[1]
no_att_count = df["Attrition"].value_counts()[0]
yes_att_count = df["Attrition"].value_counts()[1]
total_count = df["Attrition"].count()

# Setup app and layout/frontend
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
# Setup sidebar style
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 56.5,
    "left": 20,
    "bottom": 10,
    "width": "20rem",
    "padding": "3rem 1rem",
    "background-color": "#D4E6F1",
}
# Setup the main content style
CONTENT_STYLE = {
    "position": "fixed",
    "top": 56.5,
    "left": 360,
    "bottom": 10,
    # 'right': 20,
    "width": "66rem",
    "padding": "3rem 1rem",
    # "margin-left": "12rem",
    # "margin-right": "rem",
    # "padding": "2rem 1rem",
    "background-color": "#F2F3F4",
}

# Define cards for the dashboard
cards = [
    dbc.Card(
        [
            html.H2(f"{attrition_rate*100:.2f}%", className="card-title"),
            html.P("Overall Attrition Rate", className="card-text"),
        ],
        body=True,
        color="light",
    ),
    # This can be replaced with other summary stacked-bar chart
    dbc.Card(
        [
            html.H2(f"{attrition_rate*100:.2f}%", className="card-title"),
            html.P("Overall Attrition Rate", className="card-text"),
        ],
        body=True,
        color="light",
    ),
]

app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                [html.H1(dcc.Markdown("""# **Key Factors for Employee Attrition**"""))]
            ),
            align="auto",
        ),
        # Add three widgets to the sidebar
        html.Div(
            [  
                html.Br(),
                html.Br(),
                html.H2("Dashboard Filters", className="display-10"),
                html.Hr(),
                html.Br(),
                dcc.Markdown("""_Department_"""),
                dcc.Dropdown(
                    id="depart-widget",
                    value=["Sales", "Human Resources", "Research & Development"],
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
        ),
        # Add card and plots to the dashboard
        html.Div(
            [
                dbc.Row([dbc.Col(card) for card in cards]),
                html.Br(),
                # dbc.Row(
                dbc.Col(
                    [
                        html.Iframe(
                            id="scatter",
                            style={
                                "border-width": "0",
                                "width": "200%",
                                "height": "1000px",
                                "horizontalAlign": "center",
                            },
                        )
                    ]
                )
                # )]
                # ),
            ],
            style=CONTENT_STYLE,
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
def update_graph(depart, gender, age=18):
    # filter data based on criteria
    data = df[
        (df["Department"].isin(depart))
        & (df["Gender"].isin(gender))
        & (df["Age"] >= age[0])
        & (df["Age"] <= age[1])
    ]

    # distribution on monthly income
    chart_income = (
        alt.Chart(data, title="Monthly Income Distribution")
        .mark_boxplot()
        .encode(
            x=alt.X(
                "MonthlyIncome:Q",
                scale=alt.Scale(zero=False),
                axis=alt.Axis(grid=False),
            ),
            y=alt.Y("Attrition", axis=alt.Axis(grid=False)),
            color="Attrition",
        )
        .properties(height=180, width=350)
    )

    # distribution on Work life balance
    chart_worklife = (
        alt.Chart(data, title="Work Life Balance")
        .mark_bar()
        .encode(
            y=alt.Y(
                "WorkLifeBalance:O", title=""
            ),  # scale=alt.Scale(domain=["Low", "Medium", "High", "Very High"])
            x=alt.X(
                "count()",
                stack="normalize",
                axis=alt.Axis(format="%"),
                title="Proportion",
            ),
            color="Attrition",
        )
        .properties(height=180, width=350)
    )

    # distribution on business travel frequency
    chart_travel = (
        alt.Chart(data, title="Business Travel Frequency")
        .mark_bar()
        .encode(
            y=alt.Y("BusinessTravel", title=""),
            x=alt.X(
                "count()",
                stack="normalize",
                axis=alt.Axis(format="%"),
                title="Proportion",
            ),
            color="Attrition",
        )
        .properties(height=180, width=350)
    )

    # distribution on environment satisfaction
    chart_environment = (
        alt.Chart(data, title="Environment Satisfaction")
        .mark_bar()
        .encode(
            y=alt.Y("EnvironmentSatisfaction", title=""),
            x=alt.X(
                "count()",
                stack="normalize",
                axis=alt.Axis(format="%"),
                title="Proportion",
            ),
            color="Attrition",
        )
        .properties(height=180, width=350)
    )

    chart = (chart_income & chart_travel) | (chart_worklife & chart_environment)
    return chart.to_html()


if __name__ == "__main__":
    app.run_server(debug=True, host="127.0.0.1")
