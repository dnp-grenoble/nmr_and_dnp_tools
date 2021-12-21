# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 16:17:05 2021

@author: Paul
"""
import pandas as pd
import sys
from scipy.constants import Planck
import numpy as np

nuctable=pd.read_excel('NMR_freq_table.xlsx')
gyr_ratio_MHz_T=nuctable["GyrHz"];
name_nuc=nuctable["Name"];

nuc1 = input("Enter the first nucleus: ");
nuc2 = input("Enter the second nucleus: ");

dist = float(input("Exter the distance in Angstrom: "))

nuc1idx = name_nuc[name_nuc.str.match(nuc1)].index
nuc2idx = name_nuc[name_nuc.str.match(nuc2)].index

if nuc1idx.empty == True or nuc2idx.empty == True :
    sys.exit("Nucleus not found, try to make it")

gyr1=gyr_ratio_MHz_T[nuc1idx[0]]*1e6
gyr2=gyr_ratio_MHz_T[nuc2idx[0]]*1e6

dip=-1e-7*(gyr1*gyr2*Planck)/((dist*1e-10) ** 3);
print("The dipolar coupling = " + str(np.abs(dip)) + ' Hz')
print("The dipolar coupling = " + str(np.abs(dip/1e3)) + ' kHz')