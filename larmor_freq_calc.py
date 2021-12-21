# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 18:35:05 2021

@author: Paul
"""
import pandas as pd
import sys
import numpy as np

nuctable=pd.read_excel('NMR_freq_table.xlsx')
gyr_ratio_MHz_T=nuctable["GyrHz"];
name_nuc=nuctable["Name"];

nuc1 = input("Enter the first nucleus: ");
Bfield = float(input("Enter main magnetic field in T: "));

nuc1idx = name_nuc[name_nuc.str.match(nuc1)].index

if nuc1idx.empty == True:
    sys.exit("Nucleus not found, try to make it")

gyr1=gyr_ratio_MHz_T[nuc1idx[0]]

print("The Larmor Freq is = " + str(gyr1*Bfield) + ' MHz')