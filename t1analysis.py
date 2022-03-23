#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 10:19:23 2022

@author: paul
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")
#from scipy.optimize import curve_fit
from lmfit import Model
from sympy import symbols, diff, exp, sqrt, lambdify


def twoexpbuild(x, ampl1, tau1, tau2):             
    exponential = ampl1*(1-np.exp(-x/tau1))+(1-ampl1)*(1-np.exp(-x/tau2))
    return exponential

def monoexpbuild(x, tau):
    exponential = 1-np.exp(-x/tau)
    return exponential

def stretchedexp(x, T1, beta):
    exponential = (1-np.exp(-np.power((x/T1),beta)))
    return exponential

def optimumrecycledelaytwoexp(x, ampl1, tau1, tau2):
    t, b, a, Ta, Tb = symbols ('t b a Ta Tb')
    b = 1-a
    s=a*(1-exp(-t/Ta))/sqrt(t)+b*(1-exp(-t/Tb))/sqrt(t)
    k=diff(s,t)
    y=k.subs({Ta:tau1,Tb:tau2,a:ampl1})
    lam_x = lambdify(t, y, modules=['numpy'])
    x_vals = np.linspace(1, 40, 100000)
    y_vals = lam_x(x_vals)
    return x_vals[np.argmin(abs(y_vals))]

def optimumrecycledelayoneexp(x, tau1):
    t, Ta = symbols ('t Ta')
    s=(1-exp(-t/Ta))/sqrt(t)
    k=diff(s,t)
    y=k.subs({Ta:tau1})
    lam_x = lambdify(t, y, modules=['numpy'])
    x_vals = np.linspace(1, 40, 100000)
    y_vals = lam_x(x_vals)
    return x_vals[np.argmin(abs(y_vals))]

def optimumrecycledelaystrexp(x, tau1, beta):
    t, b, Ta = symbols ('t b Ta')
    s=(1-exp(-np.power((t/Ta),b)))/sqrt(t)
    k=diff(s,t)
    y=k.subs({Ta:tau1,b:beta})
    lam_x = lambdify(t, y, modules=['numpy'])
    x_vals = np.linspace(1, 40, 100000)
    y_vals = lam_x(x_vals)
    return x_vals[np.argmin(abs(y_vals))]

    

colspecs=[(0, 10),(10, 21), (22, 35), (36, 48), (48, 61)]

df=pd.read_fwf('D:/OneDrive/Academics/Data/2021-12-CP-1H-13C-PAVLOT-Indomethacin/2/pdata/1/ct1t2.txt', skiprows=21, skipfooter=3, colspecs=colspecs, names=['Point','Tau','Expt','Calc','Difference'])

p=0

int_expt=df['Expt']
time=df['Tau']
int_calc=df['Calc']

time_array=np.zeros((time.size,1))
for i in time:
    if i[-1] in 'm':
        time_array[p]=float(i[:-1])*0.001
    else:
        time_array[p]=float(i[:-1])*1
    p+=1


plt.plot(time_array,int_expt)
plt.plot(time_array, int_calc)

ydata=int_calc.to_numpy()
xdata=time_array

# For scipy fitting
#popt, pcov = curve_fit(twoexpbuild, xdata.flatten(), ydata.flatten(), bounds=([0.01,0.1,1],[1,256,256]))
# print('a =', popt[0])
# print('b =', 1-popt[0])
# print('T1a =', popt[1])
# print('T1b =', popt[2])

choice=int(input("1 for monoexp, 2 for biexp, 3 for stretched: "))

if choice == 1:
    exp_build=Model(monoexpbuild)
    exp_build.set_param_hint('tau', value=20, min=0.001, max=256.0)
    result=exp_build.fit(ydata.flatten(),x=xdata.flatten(),method='nelder')
    plt.plot(time_array,result.best_fit,'--')
    t1=result.best_values.get("tau")
    optimumd1=optimumrecycledelayoneexp(xdata.flatten(), t1)
    plt.plot(time_array,result.best_fit,'--')
    print('T1 is '+ str(round(t1,2))+ 's')
    print('The optimum recycle delay should be: '+ str(round(optimumd1,2))+'s')
    
elif choice == 2:
    exp_build=Model(twoexpbuild)
    exp_build.set_param_hint('ampl1', value=0.5, min=0.01, max=1)
    exp_build.set_param_hint('tau1', value=0.3, min=0.001, max=256.0)
    exp_build.set_param_hint('tau2', value=100, min=10, max=256.0)
    result=exp_build.fit(ydata.flatten(),x=xdata.flatten(),method='nelder')

    a=result.best_values.get("ampl1")
    b=1-a
    t1a=result.best_values.get("tau1")
    t1b=result.best_values.get("tau2")

    optimumd1=optimumrecycledelaytwoexp(xdata.flatten(), a, t1a, t1b)
    plt.plot(time_array,result.best_fit,'--')
    print('Component 1 ' + str(round(a,2)) +'\n'+'Component 2 ' + str(round(b))+ '\n'+ 'T1 of 1 '+str(round(t1a,2))+ '\n'+ 'T1 of 2 '+str(round(t1b,2)))    
    print('The optimum recycle delay should be: '+ str(round(optimumd1,2))+'s')
elif choice == 3:
    exp_build=Model(stretchedexp)
    #exp_build.set_param_hint('a1', value=1, min=0.01, max=1)
    exp_build.set_param_hint('T1', value=10, min=0.001, max=256.0)
    exp_build.set_param_hint('beta', value=0.5, min=0, max=1)
    result=exp_build.fit(ydata.flatten(),x=xdata.flatten(),method='nelder')

    #a=result.best_values.get("a1")
    t1=result.best_values.get("T1")
    beta=result.best_values.get("beta")
    optimumd1=optimumrecycledelaystrexp(xdata.flatten(), t1, beta)
    plt.plot(time_array,result.best_fit,'--')
    print('T1 is '+str(round(t1,2)) + '\n' + 'Stretching factor ' + str(round(beta,2)))
    print('The optimum recycle delay should be: '+ str(round(optimumd1,2))+'s')
else:
    print('Invalid method')



