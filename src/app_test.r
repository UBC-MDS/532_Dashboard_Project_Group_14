library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)
library(dashBootstrapComponents)
library(ggplot2)
library(plotly)

df = read.csv("data/Processed/HR_employee_Attrition_editted.csv")

app = Dash$new(external_stylesheets = dbcThemes$BOOTSTRAP)

app$layout(
  dbcContainer(
    htmlH1('Key Factors for Employee Attrition'),
    dbcRow(
      list(
        dbcCol(
          list(
            htmlLabel('Department'),
            dccDropdown(
              id = 'depart-widget',
              value = 'Sales'
            #   options = list(list(label = col, value = col),
            #                  list(label = "San Francisco", value = "SF")),
            # )
          )
        ),
   )))))

app$run_server(debug = T)


