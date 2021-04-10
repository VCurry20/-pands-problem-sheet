# Display the plot of a function 

# Week 8

# Veronica Curry
# Student ID: G00074924


# Write a program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes
# Using Matplotlib

# Methodology
# F / G / H - are x, x2, x3  / x, x*x, x*x*x ( or x^x )
# Axis = x- 0 / y = 4 - y 4 times the value  -- random?
# import modules
# add in legends / colours / etc
# show to test / fig to save when completed

import matplotlib.pyplot as plt                                                         # import Matplotlip as plt
import numpy as np                                                                      # import numpy as np


fplot= np.array(range(0,4))                                                             # set plot f - from numpy array - range 0,4
gplot= fplot * fplot                                                                    # set plot g = x*x - fplot * fplot
hplot= fplot * fplot * fplot                                                            # set plot h = x*x*x - fplot*fplot*fplot
 
plt.plot(hplot, label='Line H', color='#6495ED', linewidth=4)                           # Plot h - with label, color and linewidth
plt.plot(gplot, label='Line G', color='#40E0D0', linewidth=4, linestyle=':')            # PLot g - with label, color, linewidth and as a dot-to-dot line
plt.plot(fplot, label='Line F', color='#9FE2BF', linewidth=4, linestyle=':')            # PLot f - with label, color, linewidth and as a dot-to-dot line

plt.title('Task Week 8', fontsize= 16)                                                  # plot title - 'title name' - font size
plt.xlabel('X Axis')                                                                    # plot x axis label - XAxis
plt.ylabel('Y Axis')                                                                    # plot y axis label - YAxis
plt.legend()                                                                            # plot add legend

plt.gca().spines['top'].set_visible(False)                                              # plot - set the spine - top - as invisible
plt.gca().spines['right'].set_visible(False)                                            # plot - set the spine - right - as invisible

plt.text(2.25,20, 'Line H')                                                             # plot txt (line name) - coordinates on graph - line name
plt.text(2.3,8, 'Line G')                                                               # plot txt (line name) - coordinates on graph - line name
plt.text(2.6,4, 'Line F')                                                               # plot txt (line name) - coordinates on graph - line name

# plt.show ()                      # show the plot / print out

plt.savefig("plotTask.png")       # save the plot



# Reference 1. https://www.infoplease.com/math-science/mathematics/algebra/behold-the-power-of-exponents
# Reference 2. https://uk.mathworks.com/matlabcentral/answers/178523-how-to-created-plot-with-three-lines
# Reference 3. Lab week 8 / Question 5 - write a program y = x2
# Reference 4. https://stackoverflow.com/questions/24547047/how-to-make-matplotlib-graphs-look-professionally-done-like-this
# Reference 5. https://towardsdatascience.com/simple-ways-to-improve-your-matplotlib-b64eebccfd5
# Reference 6. https://www.w3schools.com/colors/colors_picker.asp
# Reference 7. https://htmlcolorcodes.com/
# Reference 8. https://towardsdatascience.com/10-tips-to-improve-your-plotting-f346fa468d18
# Reference 9. https://www.pythoninformer.com/python-libraries/matplotlib/line-plots/#:~:text=You%20can%20set%20the%20width,style%20using%20the%20linestyle%20parameter.
# Reference 10. https://queirozf.com/entries/add-labels-and-text-to-matplotlib-plots-annotation-examples
# Reference 11. https://uk.mathworks.com/help/matlab/creating_plots/add-title-axis-labels-and-legend-to-graph.html






