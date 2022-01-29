# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 18:52:52 2022

@author: Paul
"""
from sympy import symbols, diff, exp, sqrt, lambdify, init_session
import matplotlib.pyplot as plt
import numpy as np
init_session()

t, b, a, Ta, Tb = symbols ('t b a Ta Tb')
b = 1-a

s=a*(1-exp(-t/Ta))/sqrt(t)+b*(1-exp(-t/Tb))/sqrt(t)
k=diff(s,t)

#pprint(s)


#pprint(k)
t1=input("Enter the first buildup time: ")
t2=input("Enter the second buildup time: ")
comp1=float(input("Enter the topspin value of the first component: "))
comp2=float(input("Enter the topspin value of the second component: "))

comp=comp1/(comp1+comp2)

y=k.subs({Ta:t1,Tb:t2,a:comp})
y2=s.subs({Ta:t1,Tb:t2,a:comp})

lam_x = lambdify(t, y, modules=['numpy'])
lam_x2 = lambdify(t, y2, modules=['numpy'])
x_vals = np.linspace(1, 40, 100000)
y_vals = lam_x(x_vals)
y2_vals = lam_x2(x_vals)

plt.plot(x_vals,abs(y_vals))
plt.plot(x_vals,abs(y2_vals))

min_x_val=x_vals[np.argmin(abs(y_vals))]

plt.plot((min_x_val,min_x_val),(0,np.max(y2_vals)),'k-.')
plt.xlabel('Time(s)')
plt.ylabel('Intensity (arb. u.)')


print('The optimum d1 should be: ' + str(x_vals[np.argmin(abs(y_vals))]))