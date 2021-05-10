# ----------------- Histogram ----------------------------------------------------
#A histogram is a graph showing frequency distributions.
#It is a graph showing the number of observations within each given interval.

# In Matplotlib, we use the hist() function to create histograms.

# For simplicity we use NumPy to randomly generate an array with 250 values, where the values will concentrate around 170, and the standard deviation is 10. 
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170,10,250) # A Normal Data Distribution by NumPy:

plt.hist(x)
plt.show()



