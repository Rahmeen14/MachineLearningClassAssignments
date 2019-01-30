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
axes = plt.gca()
def abline(slope, intercept):
    """Plot a line from slope and intercept"""
    global axes
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    return plt.plot(x_vals, y_vals)
def plotResiduals(slope, intercept, X, Y):
    for i in range(0, len(X)) :
         plt.plot([X[i], X[i]], [Y[i], slope*X[i]+intercept], '--')
def onclick(event):
    global axes
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          (event.button, event.x, event.y, event.xdata, event.ydata)) 
    Xdata.append(event.xdata)
    Ydata.append(event.ydata)
    
    if len(Xdata) > 2 :             
        axes.cla()
    if len(Xdata) > 1 :  
        for i in range(0, len(Xdata)):
            plt.plot(Xdata[i], Ydata[i], ',', marker = 'o', markersize=2)
        xbar = sum(Xdata)/len(Xdata)        
        ybar = sum(Ydata)/len(Ydata)
        xxdata = Xdata - xbar
        yydata = Ydata - ybar
        num = np.sum(np.multiply(xxdata, yydata))
        den = np.sum(np.multiply(xxdata, xxdata))
        m = num/den
        c = ybar - m*xbar
        abline(m, c)
        plotResiduals(m, c, Xdata, Ydata)
    fig.canvas.draw()
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
