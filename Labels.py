# Create Labels for a Plot
# With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.

# Add labels to the x- and y-axis:

import matplotlib.pyplot as plt
import numpy as np


x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y)

plt.xlabel('Average Plus')    # Add labels to the x-axis
plt.ylabel('Calorie Burnage') # Add labels to the y-axis

plt.show()

# --------- Create a Title for a Plot
# With Pyplot, you can use the title() function to set a title for the plot.

# -------- Add a plot title and labels for the x- and y-axis: -------

plt.plot(x,y)

plt.xlabel('Average Plus')
plt.ylabel('Calorie Burnage')

plt.title('Sports Data Watch') #  Create a Title for a Plot
plt.show()


# --------- Set Font Properties for Title and Labels  ----------------
#You can use the fontdict parameter in xlabel(), ylabel(), and title() to set font properties for the title and labels.

# Set font properties for the title and labels:

font1 = {'family':'Sans-serif','color':'blue','size':'20'}
font2 = {'family':'serif','color':'darkred','size':'15'}
font3 = {'family':'Century Gothic','color':'darkred','size':'15'}

plt.plot(x,y)
plt.title('Sports Data Watch', fontdict = font1)
plt.xlabel('Average Plus', fontdict = font2)
plt.ylabel('Calorie Burnage', fontdict = font3)

plt.show()

# ----------------- Position the Title --------------------------------
# You can use the loc parameter in title() to position the title.

# Legal values are: 'left', 'right', and 'center'. Default value is 'center'.


plt.title("Sports Watch Data", loc = 'left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.show()






