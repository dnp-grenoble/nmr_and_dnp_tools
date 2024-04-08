# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 18:52:52 2022

@author: Paul
"""

import numpy as np
import matplotlib.pyplot as plt


def relax_model(a, ta, tb, beta, xmin, xmax):
  optd1=np.empty([])
  index=np.empty([])
  x=np.linspace(xmin, xmax, 1000000)
  y=1-np.exp(-x/tb)+a*np.exp(-x/tb)-a*np.exp(-(x/ta)**beta)
  sens=y/np.sqrt(x)
  dsens = np.gradient(sens,(xmax-xmin)/1000000)
  index = np.where(np.diff(np.sign(np.squeeze(dsens))) != 0)[0] + 1
  if index.size > 0:
    optd1 = x[index]
  return x, y, sens, optd1



t1 = float(input("Enter the first buildup time: "))
t2 = float(input("Enter the second buildup time: "))
comp1 = float(input("Enter the topspin value of the first component: "))
comp2 = float(input("Enter the topspin value of the second component: "))

comp = comp1 / (comp1 + comp2)

x, y_vals, y_sens, opt_tb = relax_model(comp, t1, t2, 1.0, 0.001, 512.)




fig, ax = plt.subplots()
ax.plot(x, y_vals, label='Intensity')
ax.plot(x, y_sens, label='Sensitivity')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Intensity')
ax.legend(loc = 'best')
ax.set_ylim([0.0, 1.2])
    
if not np.shape(opt_tb):
    print("No suitable solution found, derivative has **NO** zero crossing.")
else:
    ax.axvline(x=opt_tb[0], ls = '--', lw = 0.5, c='magenta')
    ax.text(x=opt_tb[0]+5, y=1.1, s=np.round(opt_tb[0],2) , fontsize=12)
    print('The optimum recycle delay is ' + str(np.round(opt_tb[0],2)) + ' s')

plt.show()