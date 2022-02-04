# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx], idx


temp = np.linspace(20,400,4000)
y0=0.0145*np.ones(np.size(temp));
y1=5330*(temp ** -2);
y2=1.42e7*(temp ** -4);
y3=2.48e9*(temp ** -6);
y=y0+y1+y2+y3;

t1 = float(input("Enter a number:"));

plt.figure()
plt.plot(temp,y)
plt.plot((temp[1], temp[np.size(temp)-1]), (t1, t1), 'k.-')


k, l=find_nearest(y, t1)

print(temp[l])