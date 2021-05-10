#---------------Linestyle -----------------------
# The keyword argument linestyle, or shorter ls, to change the style of the plotted line:
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()

#-------------Use a dashed line: -----------------
plt.plot(ypoints, linestyle = 'dashed')
plt.show()


#---------------Shorter Syntax --------------------
# The line style can be written in a shorter syntax:

plt.plot(ypoints, ls = ''or'') # linestyle can be written as "ls" ; dotted => ':'; solid (default) => '-';'dashdot'=>'-.'; dashed => '--' and 'None'=>'' or ' '
plt.show()

#------------------- Line color -------------------

# the keyword argument color or the shorter c to set the color of the line:

plt.plot(ypoints, ls = ':', c = 'r')
plt.show()

# ---- Plot with a beautiful green dashdot line: -----------

plt.plot(ypoints, ls = '-.', c = '#4CAF50') # 
plt.show()

#------ Plot with the color named "hotpink":

plt.plot(ypoints, c = 'hotpink')
plt.show()

#--------------- Line Width -----------------------------------
# The keyword argument linewidth or the shorter lw to change the width of the line.
# The value is a floating number, in points:

plt.plot(ypoints, c ='b', lw ='20')
plt.show()

# ------------------ Multiple Lines -----------------------------
# You can plot as many lines as you like by simply adding more plt.plot() functions:
# Draw two lines by specifying a plt.plot() function for each line:

y1 = np.array([3,8,1,10])
y2 = np.array([6,2,7,11])

plt.plot(y1)
plt.plot(y2)

plt.show()

# ---- You can also plot many lines by adding the points for the x- and y-axis for each line in the same plt.plot() function.

# (In the examples above we only specified the points on the y-axis, meaning that the points on the x-axis got the the default values (0, 1, 2, 3).)

# The x- and y- values come in pairs:

# Draw two lines by specifiyng the x- and y-point values for both lines:

x1 = np.array([0,1,2,3])
x2 = np.array([0,1,2,3])

plt.plot(x1,y1,x2,y2)
plt.show()




