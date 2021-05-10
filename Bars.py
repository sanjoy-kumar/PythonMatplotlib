# -------------- Creating Bars
# With Pyplot, you can use the bar() function to draw bar graphs:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A','B','C','D'])
y = np.array([3,8,1,10])

plt.bar(x,y)
plt.show()


# ---------------------- Horizontal Bars ---------------------------
# If you want the bars to be displayed horizontally instead of vertically, use the barh() function:

plt.barh(x,y)
plt.show()

# ----------------------- Bar Color ---------------------------------
# The bar() and barh() takes the keyword argument color to set the color of the bars:

plt.bar(x,y, color = 'hotpink') # Color Names
plt.show()

plt.barh(x,y, color = '#4CAF50') # Color Hex
plt.show()

# --------------------- Bar Width -----------------------------------
# The bar() takes the keyword argument width to set the width of the bars:

plt.bar(x,y, width = 0.1) # The default width value is 0.8
plt.show()

plt.barh(x,y, height = 0.4) # For horizontal bars, use height instead of width. The default height value is 0.8
plt.show()





