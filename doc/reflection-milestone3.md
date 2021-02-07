Reflection - Milestone3
================
Cheuk Ho, Hazel Jiang, Anita Li, Ivy Zhang

30/01/2021

Following our proposal and python version, we deployed our dashboard in R offering users three options of filtering `Department`, `Gender` and `Age` to see how different factors (`Monthly Income`, `Work Life Balance`, `Business Travel` and `Environment Satisfaction`) contribute to employee attrition based on IBM employee satisfaction survey data. Our interactive dashboard enables users to see the attrition among 4 key factors for different employee segments, which could help our users to develop their action plan for next step.
 
We are able to implement most of what we have done in the proposal and python to the R dashboard, and our users are able to see the attrition in proportions among the `WorkLife Balance`, `Environment Satisfaction` and `Frequency of Business Travel` plots and different quantile information in the `Monthly Income` plot. In In addition，interactivity such as tooltip and zoom-in are enabled with ggplotly in our R implementation
 
However, during our implementation of our proposal, we encountered some problems as well. We encounter problem with the 2 drop-down widgets where it will have layout error if we clear the drop-down. Instead of having empty plots, the plot will stuck with latest plot result. We will look into this along with the function of showing total data with empty value in drop down. Another problem we had was that we were not able to add legend to the plots due to using subplot.  Right now, we are using text with different colors to present attrited/not attrited. Our intention is to find other ways like using `cowplot` or using different column outputs in layout setting to bring back the legend.
 
We haven’t received any feedbacks yet, but comparing to the dashboard we published using Python, we have implemented a better color scheme for our plots, which makes the presentation more pleasant. However, we still believe that for future improvements, it can be useful to add one or two empty plots that allow users to choose other variables (numerical and categorical) to plot against attrition offering them more flexibility in exploring the data base on their needs and interests. We will try to fix about glitch and  incorporate feedback when it comes in Milestone 4.
