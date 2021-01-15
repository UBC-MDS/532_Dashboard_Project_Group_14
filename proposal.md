# IBM Employee Attrition Analytics
- author: DSCI 5 Group14
- Group Member: Cheuk Ho, Hazel Jiang, Anita Li, Ivy Zhang

## Motivation and Purpose

Our role: Data scientist consultancy firm

Target audience: Health care administrators

Missed medical appointments cost the healthcare system a lot of money and affects the quality of care. If we could understand what factors lead to missed appointments it may be possible to reduce their frequency. To address this challenge, we propose building a data visualization app that allows health care administrators to visually explore a dataset of missed appointments to identify common factors. Our app will show the distribution of factors contributing to appointment show/no show and allow users to explore different aspects of this data by filtering and re-ordering on different variables in order to compare factors that contribute to absence.



## Description of the Data

We will be visualizing a dataset of approximately 300,000 missed patient appointments. Each appointment has 15 associated variables that describe the patient who made the appointment (patient_id, gender, age), the health status (health_status) of the patient (Hypertension, Diabetes, Alcohol intake, physical disabilities), information about the appointment itself (appointment_id, appointment_date), whether the patient showed up (status), and if a text message was sent to the patient about the appointment (sms_sent). Using this data we will also derive a new variable, which is the predicted probability that a patient will show up for their appointment (prob_show).

## Research Questions and Usage Scenarios

The app contains a landing page that shows the distribution (depending on data type, bar chart, density chart etc) of dataset factors (hypertension, physical disabilities etc.) colored coded according to whether patients showed up or didn't show up for an appointment. From a dropdown list, users can filter out variables from the distribution display, by patient demographics (i.e. only show female patients), by appointment data (i.e. if SMS was sent), and finally by the date range of appointments. A different dropdown menu will allow users to re-order variables according to the probability of patients being a no-show or in alphabetical order to comorbidities. Users can compare the distribution of co-morbidities by scrolling down through the app interface.


  
## License
IBM Employee Attrition Analytics materials here are licensed under the Creative Commons Attribution 2.5 Canada License (CC BY 2.5 CA). If re-using/re-mixing please provide attribution and link to this webpage.

## References

Saishruthi Swaminathan, Richard Hagarty. “Data science process pipeline to solve employee attrition”, Data Science Community, IBM. https://developer.ibm.com/patterns/data-science-life-cycle-in-action-to-solve-employee-attrition-problem/#description.
