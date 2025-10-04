'''import matplotlib.pyplot as plt
yr =[1994 ,1995 , 1996, 1997 , 1998, 1999, 2000]
tm = [2,4,6,8,10,12,14]
plt.scatter(yr,tm)
#plt.plot(yr,tm)
plt.show()'''

import matplotlib.pyplot as plt

# Sample data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5]

# Create histogram with 3 bins
plt.hist(data, bins=3)

# Display the histogram
plt.show()