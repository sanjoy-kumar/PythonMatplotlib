# Display Multiple Plots
# With the subplot() function you can draw multiple plots in one figure:

# -------------------- Draw 2 plots: ----------------------

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1,2,1) # The layout is organized in rows and columns, which are represented by the first and second argument. The third argument represents the index of the current plot.
plt.plot(x,y)


#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1,2,2) # #the figure has 1 row, 2 columns, and this plot is the second plot.
plt.plot(x,y)


plt.show()


# ------------------------ Draw 2 plots on top of each other: ---------------

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2,1,1)
plt.plot(x,y)


#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2,1,2)
plt.plot(x,y)

plt.show()

# ------------------- Draw 6 plots: ------------------------------------------

#Plot 1
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2,3,1)
plt.plot(x,y)

# Plot 2

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2,3,2)
plt.plot(x,y)

#Plot 3

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2,3,3)
plt.plot(x,y)

#Plot 4

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2,3,4)
plt.plot(x,y)

#Plot 5
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2,3,5)
plt.plot(x,y)

#plot 6

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2,3,6)
plt.plot(x,y)

plt.show()

#------------------ Title
# You can add a title to each plot with the title() function:

# 2 plots, with titles:

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1,2,1)
plt.plot(x,y, marker = "o", ms = 20, mec = 'r')
plt.title("Sales")


#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1,2,2)
plt.plot(x,y, marker = "*", ms = 20,mfc ='r')
plt.title("Income")

plt.show()


# ----------------------- Super Title ----------------------------------
# You can add a title to the entire figure with the suptitle() function:


#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1,2,1)
plt.plot(x,y, marker = "o", ms = 20, mec = 'r')
plt.title("Sales")


#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1,2,2)
plt.plot(x,y, marker = "*", ms = 20,mfc ='r')
plt.title("Income")

plt.suptitle("My Shop")
plt.show()


