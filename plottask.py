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

import matplotlib.pyplot as plt 
import numpy as np 


fplot= np.array(range(0,4))
gplot= fplot * fplot
hplot= fplot * fplot * fplot

plt.plot(fplot, label='Line F', color='#00FFFF', linewidth=4)
plt.plot(gplot, label='Line G', color='#ff66d9', linewidth=4)
plt.plot(hplot, label='Line H', color='#ffff66', linewidth=4)

plt.title('Task Week 8')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.text(2.25,20, 'Line H')
plt.text(2.3,8, 'Line G')
plt.text(2.6,4, 'Line F')

plt.show ()                      # show the plot / print 

#plt.savefig("plotTask.png")       # save the plot



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





