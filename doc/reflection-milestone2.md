Reflection - Milestone2
================
Cheuk Ho, Hazel Jiang, Anita Li, Ivy Zhang

22/01/2021

In this milestone, we implemented the plots for the 4 key factors (`Monthly Income`,
`Work Life Balance`, `Business Travel` and `Environment Satisfaction`)
that contributes to employee attrition based on IBM
employee satisfaction survey data. We also implemented a total of 
3 interactive widgets to our app, 2 drop-down filters (`Department` and `Gender`) 
and 1 slider (`Age`) for the management team to play with in order to see 
whether the attrition rate varies between features. By filtering the data by these widgets, 
our plots show the attrition among the 4 key factors among different employee segments, 
which could help the users to develop their action plan for next step.

We planned four widgets in our proposal, but we decided to left out `Job Role` 
drop-down widget to prevent the dashboard from showing blank plots when the `Job Role` 
is conflicting with `Department` drop-down widget, which would negatively impact on the digest 
of the insight and user experience. As the `Job Role` is highly dependent on the `Department`, 
keeping only `Department` in our widget list would be sufficient for the key analysis.
Another thing we have not implemented is that for now
our default plots are showing the attrition based on female in sales
department with age between 18 to 60. We would like to make the default
plots to show the attrition proportion among all the data instead of
filtered data. We are hoping to implement this in the
future milestone. We also identified an issue with altair plotting 
the ordinal categorical variable in alphabetical order. Changing it
with domain attribute of the plot scale is having conflict with Dash. 
Now we have relabeled them with number in order to show the desired order.
We will try to figure out a better way in the next 2 milestones. 

Our user-interactive dashboard demonstrates a comprehensive overview 
of how employee's attrition distributes in four key aspects with clear and straight 
forward plots that allows users to read off the key insights easily. The navigation 
and interface of our app is also very user friendly. Although our dashboard 
does a good job on many aspects, there are still area of improvement. 
We would want to further enhance the color scheme of our plot and are considering 
to add interaction locally in each plots. While we have shown the users the 
key factors for attribution, users may be interested in exploring other key factors 
that may play a role to employee attrition. For future improvements, it can be helpful 
to add one or two empty plots that allow users to choose the variables (numerical and categorical) 
to plot against attrition offering them more flexibility in exploring the data base
on their needs and interests.
