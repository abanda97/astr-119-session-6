#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


x = np.arange(0, 5, 0.1) #create x = [0..5] in 0.1 increments
y = np.sin(x)            #y = sin(x)
plt.plot(x,y)            #make a plot
plt.xlabel('x')          #label x axis
plt.ylabel('sin(x)')     #label y axis
plt.show()               #show the plot on the screen


# In[ ]:


#Save an image as png
x = np.arange(0, 5, 0.1) #create x = [0..5] in 0.1 increments
y = np.sin(x)            #y = sin(x)
plt.plot(x,y)            #make a plot
plt.xlabel('x')          #label x axis
plt.ylabel('sin(x)')     #label y axis
plt.savefig('sinx.png', bbox_inches="tight", dpi=600) #Save figure as png


# In[ ]:


#Save an image as pdf
x = np.arange(0, 5, 0.1) #create x = [0..5] in 0.1 increments
y = np.sin(x)            #y = sin(x)
plt.plot(x,y)            #make a plot
plt.xlabel('x')          #label x axis
plt.ylabel('sin(x)')     #label y axis
plt.savefig('sinx.pdf', bbox_inches="tight", dpi=600) #Save figure as png
            #can change to .pdf


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


#Make a multipanel plot with matplotlib
x = np.linspace(0,2*np.pi,100)
print(x[-1],2*np.pi)

y = np.sin(x)

