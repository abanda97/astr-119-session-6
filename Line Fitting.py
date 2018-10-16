#!/usr/bin/env python
# coding: utf-8

# # Example of performing linear least squares fitting

# ### First we import numpy and matplotlib as usual

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np


# ## Now let's generate some random data about a trend line

# In[ ]:


#Set a random number seed
np.random.seed(119)

#Set number of data points
npoints = 50

#Set x
x = np.linspace(0,10.,npoints)

#Set slope, intercept, and scatter rms
m = 2.0
b = 1.0
sigma = 2.0

#Generate y points
y = m*x + b + np.random.normal(scale=sigma, size=npoints) #scale=sigma is the rms value of a gaussian, so we're generating gaussian noise
y_err = np.full(npoints, sigma) #This means there are 50 two values to fill the array(?)


# ### Let's just plot the data first to make sure the plot works

# In[ ]:


f = plt.figure(figsize=(7,7))
plt.errorbar(x,y,sigma,fmt='o')
plt.xlabel('x')
plt.ylabel('y')


# ### Method #1, polyfit()

# In[ ]:


m_fit, b_fit = np.poly1d(np.polyfit(x, y, 1, w = 1./y_err)) #weight with uncertainties
print(m_fit, b_fit)

y_fit = m_fit * x * b_fit


# ### Plot result

# In[ ]:


f = plt.figure(figsize=(7,7))
plt.errorbar(x,y, yerr=y_err, fmt='o', label='data')
plt.plot(x,y_fit,label='fit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=2, frameon=False)


# In[ ]:




