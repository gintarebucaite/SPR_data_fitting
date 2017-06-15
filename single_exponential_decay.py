
# coding: utf-8

# In[1]:

import numpy as np
#this imports numerical python library and creates a shortname for it ('np)

import matplotlib.pyplot as plt 
#this imports python plotting library and creates a shortname for it ('plt')

import matplotlib.ticker as plticker
#this imports python graph tick locator 

from scipy.optimize import curve_fit
#this imports curve_fit function from scipy package

from openpyxl import Workbook
#imports workbook function to allow data exports

from graph_plotting import graph_presentation, graph_publication
#wrote a separate script for plotting, named 'graph_plotting' and have it in my folder.

raw_data = "alng4h2all25dissociation_diff_zero.txt"
#create a variable called raw_data so that this is the only place where you'll need to put the name
#of the file you want to open (make sure you imported it into your python notebook first)

data = np.loadtxt(open(raw_data), dtype = np.float64, skiprows = 1)
#define the data type which you'll load, and tell how many rows to skip when you open it (for skipping headings etc.)

def single_exp_decay_fit(x_axis, y_axis):
    #now we tell the script something about the system to get better fits faster. This includes bounds and
    #initial values to be used in the fitting
    
    bounds = ([0, 0], [y_axis[0]+2, np.inf])
    
    #can change the bounds here without retyping everything again. can comment the 'bounds' out 
    #if not required. might need to change the upper bounds values if fit isn't too good.
        
    p0_A1 = y_axis[0]
    #this picks the first data point in column being fitted.
    
    p0_t1 = 1000 
    #let's go random
    
    p0 = [p0_A1, p0_t1]
    #p0 are the initial values for A1(first number) and t1 (second number) the script will try
    #to fit
    
    #now we tell the script how to deal with failures... it tries fitting the function,
    #and if it doesn't fit it tells us so.
   
    try: 
        popt, pcov = curve_fit(single_exp_decay, x_axis, y_axis, p0 = p0, bounds = bounds)
        #popt is fitted values and pcov are the error values. 
        #the variables go as this: *type of the fit; *the function we chose to use; *x axis; *y axis;
        #*initial variable values to be used in the fit; *bounds. it is always in this order.

        print("A1 = {0}, t1 = {1}".format(*popt))
        #print the Beq and kobs values from the best fit

        perr = np.sqrt(np.diag(pcov))
        print("A1+- = {0}, t1+- = {1}".format(*perr))
        #print one standard deviation errors on the parameters

        plt.plot(x_axis, single_exp_decay(x_axis, *popt), 'r-', x_axis, y_axis, 'b-', label = 'fit')
        plt.show()
        #plot the graph of the fit (in red) and the data (in blue)

    except:
        print ('fitting for column {} failed'.format(column))
        popt = ['fitting failed']
        perr = ['fitting failed']
    
    result = [column, *popt, *perr]
    results.append(result)
    #create a list for results and include the column numbers, fit values and errors in there.

    #print (result)

def single_exp_decay(x, A1, t1):
    return A1*np.exp(-x/t1) + 0
 


x_time_zero = data[0,0]
zeroed_data = np.copy(data)
for row in zeroed_data:
    row[0] = row[0] - x_time_zero 
#this one subtracts the first time point value from every other

   

graph_presentation(zeroed_data[:, [0]], data[:, 1::2], 'Response, RU', 'Time, s', 
                   '{}_pres.svg'.format(raw_data.split('.')[0]))

graph_publication(zeroed_data[:, [0]], data[:, 1::2], 'Response, RU', 'Time, s', 
                   '{}_pub.svg'.format(raw_data.split('.')[0]))


results = []
#create a list called 'results'




for column in range(1, len(zeroed_data[0]), 2):   
    #change the first number in () to change the column from which you start fitting
    
    print ('now fitting column no {}.'.format(column))
    #this prints the number of the column that is being fitted. 
    
    x_axis = zeroed_data[:, 0]
    y_axis = zeroed_data[:, column]
    single_exp_decay_fit(x_axis, y_axis)
 
   
    
wb = Workbook()
dest_filename = '{}.xlsx'.format(raw_data.split('.')[0])
#split the raw_data file name into two parts: the name and .txt extension. [0] is required
#because we use the first part of the split name 
ws1 = wb.active
ws1.title = 'results'
single_kobs_header = ['column', 'A1', 't1', 'A1+-', 't1+-'] 

ws1.append(single_kobs_header)

for result in results:
    ws1.append(result)
    
wb.save(filename = dest_filename)
print (dest_filename)
#print (x_time_zero)


# In[12]:

[1,2,3]*2


# In[ ]:




# In[ ]:





# In[ ]:




# In[ ]:



