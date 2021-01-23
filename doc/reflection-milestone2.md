Reflection - Milestone2
================
Cheuk Ho, Hazel Jiang, Anita Li, Ivy Zhang
22/01/2021

In this milestone, we implemented the plots for the 4 key factors (`Monthly Income`,
`Work Life Balance`, `Business Travel` and `Environment Satisfaction`)
that contributes to employee attrition based on IBM
employee satisfaction survey data. We also implemented a total of 
3 interactive widgets to our app, 2 dropdown filters (`Department` and `Gender`) 
and 1 slide bar (`Age`) for the management team to play with in order to see 
whether the attrition rate vary between features. By filtering the data, our plots 
show the attrition among the 4 key factors among different employee segment, which could help the
management team to develop their action plan for next step.

We have four widgets in our proposal but we decided to only 
implement three of them. We left out `Job Role` feature because this
feature is depending on `Department` feature. The selected job role
needs to be belong to the selected department for the dashboard to have
data to plot, otherwise we could only get empty plots. Also, the sample size for 
specific roles is quite small and regrouping them may just become another department oriented variable. 
Therefore, in this milestone, we dropped `Job Role` and only kept `Department` in the
filter session. Another thing we have not implemented is that for now
our default plots are showing the attrition based on female in sales
department with age between 18 to 60. We would like to make the default
plots to show the attrition proportion among all the data instead of
filtered data. We are hoping to implement this in the
future milestone. We also identified an issue with altair plotting 
the ordinal categorical variable in alphabetical order. Changing it
with domain attribute of of the plot scale is having conflict with Dash. 
Now we have relabeled them with number in order to show the desired order,
we will try to figure out a better way in the next 2 milestones. 

We believe our dashboard provide a general picture of how attrition rate
varies among different features based on the 4 key factors we observed.
Our plots are very clear and straight forward in terms of showing the
results. The app is very easy to play with and the layout is easy to
understand as well. Although our dashboard does a good job on many
aspects, there are still area of improvement. We would want to further enhance 
the color scheme of our plot and are considering to add interaction locally in each plot.
While we have shown the management the 4 key factors for attribution, 
users may be interested in exploring other key factors that may play a role to employee attrition. 
For future improvements, it can be helpful to add one or two empty plots that allow 
users to choose the variables (numerical and categorical) to plot against attrition 
offering them more flexibility in exploring the data base
on their needs and interested.
