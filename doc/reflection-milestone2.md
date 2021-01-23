reflection-milestone2
================
Cheuk Ho, Hazel Jiang, Anita Li, Ivy Zhang
22/01/2021

In this milestone, we implemented the 4 key factors (`Monthly Income`,
`Work Life Balance`, `Business Travel` and `Environment Satisfaction`)
that we believe will contribute to employee attrition based on IBM
employee satisfaction survey data. We also implemented 2 dropdown
filters (`Department` and `Gender`) and 1 slide bar (`Age`) for the
management team to play with in order to see whether the attrition rate
vary between features. By filtering the data, our plots show the
proportion of attrition among the 4 key factors, which could help the
management team to make better decisions.

There are two things we have in mind but not yet implemented
successfully. We have four widgets in our proposal but we are only able
to implement three of them. We left out `Job Role` feature because this
feature has interaction with `Department` feature. The selected job role
has to be included in the selected department for the dashboard to have
data to plot, otherwise we could only get empty plots. Therefore, in
this milestone, we dropped `Job Role` and only kept `Department` in the
filter session. Another thing we have not implemented is that for now
our default plots is showing the attrition based on female in sales
department with age between 18 to 60. We would like to make the default
plots to show the attrition proportion among all the data instead of
filtered data. We are hoping to implement those two aspects in the
future milestone.

We believe our dashboard provide a general picture of how attrition rate
varies among different features based on the 4 key factors we picked.
Our plots are very clear and straight forward in terms of showing the
results. The app is very easy to play with and the layout is easy to
understand as well. Although our dashboard does a good job on many
aspects, there are still limitations to it. There may exist other key
factors that play an important role to employee attrition, which are not
included in our dashboard. There are also many other features we could
try to filter to better learn the pattern of the attrition. For future
improvements, it is helpful to add one or two empty plots that allow the
users to choose the variables for x and y axis based on their concerns
toward attrition. This will offer the management team more flexibility
on their interests and give them more control to focus on what they
believe is the key factors and features against attrition.
