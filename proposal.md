# IBM Employee Attrition Analytics
- author: DSCI 5 Group14
- Group Member: Cheuk Ho, Hazel Jiang, Anita Li, Ivy Zhang

## Motivation and Purpose

Our role: Data scientist consultancy firm

Target audience: Health care administrators

Missed medical appointments cost the healthcare system a lot of money and affects the quality of care. If we could understand what factors lead to missed appointments it may be possible to reduce their frequency. To address this challenge, we propose building a data visualization app that allows health care administrators to visually explore a dataset of missed appointments to identify common factors. Our app will show the distribution of factors contributing to appointment show/no show and allow users to explore different aspects of this data by filtering and re-ordering on different variables in order to compare factors that contribute to absence.



## Description of the Data

We will be visualizing a dataset of the survey result of approximately 1470 employees. Each result(a employee) has 35 associated variables that describe their demographics (e.g. `age`, `gender`, `marital status`), their role within the company (e.g. `department`, `job title`, `job level`, `total working year`), their compensation and working status(e.g. `monthly income`, `provision of training (time)`, `frequency of business travel`, `level of work life balance`) and their attitude toward the company (e.g. `job satisfaction`, `environment satisfaction`, `relationship satisfaction`). There is quite a good mix of numerical and categorical variables. Having conduct a EDA in looking for key factors for attribution, we found that `monthly income`, `level of work level balance`, `frequency of business travel` and `environment satisfaction` seem to be the more prominent factors for attrition. We will used them as the KPIs for the dashboard app.


## Research Questions and Usage Scenarios

The app contains a landing page that shows the distribution (depending on data type, bar chart, density chart etc) of dataset factors (hypertension, physical disabilities etc.) colored coded according to whether patients showed up or didn't show up for an appointment. From a dropdown list, users can filter out variables from the distribution display, by patient demographics (i.e. only show female patients), by appointment data (i.e. if SMS was sent), and finally by the date range of appointments. A different dropdown menu will allow users to re-order variables according to the probability of patients being a no-show or in alphabetical order to comorbidities. Users can compare the distribution of co-morbidities by scrolling down through the app interface.


  
## License
IBM Employee Attrition Analytics materials here are licensed under the Creative Commons Attribution 2.5 Canada License (CC BY 2.5 CA). If re-using/re-mixing please provide attribution and link to this webpage.

## References

Saishruthi Swaminathan, Richard Hagarty. “Data science process pipeline to solve employee attrition”, Data Science Community, IBM. https://developer.ibm.com/patterns/data-science-life-cycle-in-action-to-solve-employee-attrition-problem/#description.
