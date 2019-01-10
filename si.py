# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 06:49:38 2019

@author: rahmeen
"""


import matplotlib.pyplot as plt
import  numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
Xdata = []
Ydata  = []
Xdatadif = []
Ydatadif = []
num = []
den = []
index = 0
line, = plt.plot(10,10)
def abline(slope, intercept):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    return plt.plot(x_vals, y_vals, '--')
def onclick(event):
    global line
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          (event.button, event.x, event.y, event.xdata, event.ydata)) 
    Xdata.append(event.xdata)
    Ydata.append(event.ydata)
    plt.plot(event.xdata, event.ydata, ',', marker = 'o', markersize=10)
    #plt.setp(p, markersize=100)
    if len(Xdata) > 2 :             
        line.remove()
    if len(Xdata) > 1 :   
        xbar = sum(Xdata)/len(Xdata)        
        ybar = sum(Ydata)/len(Ydata)
        xxdata = Xdata - xbar
        yydata = Ydata - ybar
        num = np.sum(np.multiply(xxdata, yydata))
        den = np.sum(np.multiply(xxdata, xxdata))
        m = num/den
        c = ybar - m*xbar
        line, = abline(m, c)
    fig.canvas.draw()

cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
