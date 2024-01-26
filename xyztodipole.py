# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 12:43:38 2022

@author: Paul
"""
import pandas as pd
import chemcoord as cc
import os
import numpy as np
from scipy.constants import Planck
from scipy.spatial.transform import Rotation as R

def anglebetweenvec (vec1, vec2):
    vec1 = vec1/np.linalg.norm(vec1)
    vec2 = vec2/np.linalg.norm(vec2)
    cp=np.cross(vec1,vec2)
    dp=np.dot(vec1,vec2)
    cosine_ang=dp
    ssc = np.array([[0,-cp[2],cp[1]],[cp[2],0,-cp[0]],[-cp[1],cp[0],0]])
    rot_mat = np.identity(3)+ssc+np.dot(ssc,ssc)/(1+cosine_ang)
    ff=R.from_matrix(rot_mat)
    eul=ff.as_euler('zyz',degrees='True')
    return eul
    
    

nuctable=pd.read_excel('NMR_freq_table.xlsx')
gyr_ratio_MHz_T=nuctable["GyrHz"];
name_nuc=nuctable["Name"];
nuc_symb=nuctable["Symbol"]

cur_dir = os.getcwd()
xyz_dir = os.chdir('amino_acids_xyz')


gly = cc.Cartesian.read_xyz('L-Alanine.xyz', start_index=1)
coord_gly = gly[['x','y','z']].to_numpy()

gyr_gly_atom=np.array([])
atom_name_list=gly['atom'].to_numpy()
l=nuc_symb.to_numpy()
for i in range(0, np.shape(coord_gly)[0]):
    choice = name_nuc.iloc[np.where(l==atom_name_list[i])]
    kk=choice.count()
    if kk > 1:
        while kk > 1:
            print("Which nucleus do you want?")
            print(choice)
            isotope_choice = input("Exact choice please: ")
            if isotope_choice in choice.unique():
                gyr_gly_atom=np.append(gyr_gly_atom,gyr_ratio_MHz_T.iloc[np.where(isotope_choice == name_nuc)].to_numpy())
                print(gyr_gly_atom)
                kk = 1
    else:
        gyr_gly_atom=np.append(gyr_gly_atom,gyr_ratio_MHz_T.iloc[np.where(choice.item() == name_nuc)].to_numpy())

dist=np.zeros([np.shape(coord_gly)[0],np.shape(coord_gly)[0]])
dip=np.zeros([np.shape(coord_gly)[0],np.shape(coord_gly)[0]])
for i in range(0, np.shape(coord_gly)[0]):
    gyr1=gyr_gly_atom[i]*1e6
    for j in range(i+1, np.shape(coord_gly)[0]):
        dist[i][j]=np.sqrt(np.sum((coord_gly[i]-coord_gly[j])**2))
        gyr2=gyr_gly_atom[j]*1e6
        dip[i][j]=-1e-7*(gyr1*gyr2*Planck)/((dist[i][j]*1e-10) ** 3);


np.set_printoptions(precision=3)
for i in range(0, np.shape(coord_gly)[0]):
    for j in range(i+1, np.shape(coord_gly)[0]):
        eulo=np.round(anglebetweenvec(coord_gly[i], coord_gly[j]),2)
        print(i+1,j+1,np.round(dip[i][j],2),*eulo,atom_name_list[i],atom_name_list[j])

        




        