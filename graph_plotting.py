
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt 
#this imports python plotting library and creates a shortname for it ('plt')

import matplotlib.ticker as plticker
#this imports python graph tick locator 



def graph_presentation(x_axis, y_axis, x_label, y_label, graph_name):
    #defines graph style if you want to put it into presentations, posters, etc. i.e. BIG NUMBERS
    
    
    plt.plot(x_axis, y_axis, linewidth = 2)
    plt.ylabel(x_label, fontsize = 14, weight = 'heavy')
    plt.xlabel(y_label, fontsize = 14, weight = 'heavy')
    #give the x and y axis a label
    #minortick_loc = plticker.AutoMinorLocator(n=3)
    #define the frequency on minor ticks
    #plt.minorticks_on()
    #turn the minor ticks on
    ax = plt.gca()
    ax.xaxis.set_minor_locator(minortick_loc)
    ax.yaxis.set_minor_locator(minortick_loc)
    [i.set_weight(550) for i in ax.get_xticklabels()]
    #set the thickness of the labels for x axis
    [i.set_weight(550) for i in ax.get_yticklabels()]
    #set the thickness of the labels for y axis
    ax.tick_params(which = 'major', direction = 'in', labelsize = 14, length = 7, width = 1.5)
    ax.tick_params(which = 'minor', direction = 'in', labelsize = 14, length = 5, width = 1.5)
    #define the appearance of the ticks
    [i.set_linewidth(1) for i in ax.spines.values()]
    
    plt.savefig(graph_name, dpi = 1200)
    plt.show()
    
def graph_publication(x_axis, y_axis, x_label, y_label, graph_name):
    #defines graph style if you want to put it into publications, reports, etc. i.e. pretty
    
    
    plt.plot(x_axis, y_axis, linewidth = 1.5)
    plt.ylabel(x_label, fontsize = 12, weight = 'medium')
    plt.xlabel(y_label, fontsize = 12, weight = 'medium')
    #give the x and y axis a label
    #minortick_loc = plticker.AutoMinorLocator(n=3)
    #define the frequency on minor ticks
    #plt.minorticks_on()
    #turn the minor ticks on
    ax = plt.gca()
    ax.xaxis.set_minor_locator(minortick_loc)
    ax.yaxis.set_minor_locator(minortick_loc)
    [i.set_weight(500) for i in ax.get_xticklabels()]
    #set the thickness of the labels for x axis
    [i.set_weight(500) for i in ax.get_yticklabels()]
    #set the thickness of the labels for y axis
    ax.tick_params(which = 'major', direction = 'in', labelsize = 12, length = 5, width = 1)
    ax.tick_params(which = 'minor', direction = 'in', labelsize = 12, length = 3, width = 1)
    #define the appearance of the ticks
    [i.set_linewidth(1) for i in ax.spines.values()]
    
    plt.savefig(graph_name, dpi = 1200)
    plt.show()





# In[6]:

[1,2,3]*2


# In[ ]:





# In[ ]:



