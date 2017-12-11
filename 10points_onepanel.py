# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 14:02:55 2017

@author: huimin,xiaojian 
CCB_fig_11 on one panel with different colored dots
"""
import numpy as np
import matplotlib.pyplot as plt

FNCL='necscoast_worldvec.dat'
CL=np.genfromtxt(FNCL,names=['lon','lat'])

fig=plt.figure(figsize=(10,9))

lon1=np.linspace(-70.45,-70.2,10)
lat1=np.linspace(42.05,41.8,10)
plt.plot(CL['lon'],CL['lat'])
plt.axis([-70.8,-69.9,41.52659,42.562711])
plt.scatter(lon1,lat1,color='red',s=7)

label=['A','B','C','D','E','F','G','H','I','J']
dian=['a','b','c','d','e','f','g','h','i','j']

for a in np.arange(len(label)):
    plt.text(lon1[a]-0.05,lat1[a]-0.03,label[a],fontsize=12)

lat=np.linspace(41.8,42.4,10)
lon=np.linspace(-70.15,-70.75,10)
plt.scatter(lon,lat,color='green',s=7)

for a in np.arange(len(lon)):
    plt.text(lon[a]+0.02,lat[a],dian[a],fontsize=12)

plt.savefig('points_wind&temp',dpi=400)

