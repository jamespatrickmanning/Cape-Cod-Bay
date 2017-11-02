# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 14:55:33 2017

@author: huimin
from xiaojian CCB_fig10c
"""
import numpy as np
import datetime as dt
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import csv
import numpy as np
from datetime import datetime,timedelta
import matplotlib.pyplot as plt
from math import sqrt
from netCDF4 import Dataset



fig=plt.figure(figsize=(18,15))
#fig,axes=plt.subplot(3,2,sharex=True,sharey=True)

FNCL='necscoast_worldvec.dat'
CL=np.genfromtxt(FNCL,names=['lon','lat'])

#-------------------first
ax1=fig.add_subplot(3,2,1)
c1 = np.genfromtxt('strandings_1991_only_town.csv',dtype=None,names=['turtle_ID','date','town'],delimiter=',',skip_header=1)
c1['town']=np.char.capitalize(c1['town'])
towns1=[]
for a in c1['town']:
    print a
    if a not in towns1:
        towns1.append(a)
num1=[]
for a in np.arange(len(towns1)):
    j=0
    for b in np.arange(len(c1['town'])):
        if towns1[a]==c1['town'][b]:
            j=j+1
    num1.append(j)
            
    #towns1[a]
lon1=[-70.3625,-70.0455,-69.95,-70.3508,-70.9333,-70.7017,-70.1692,-70.0867,-70.0453,-70.9181]
lat1=[41.7251,41.7512,41.7011,41.6339,41.4167,41.5167,42.0175,42.0376,41.8959,41.4333]
#FNCL='necscoast_worldvec.dat'
# lon lat pairs
# segments separated by nans

#CL=np.genfromtxt(FNCL,names=['lon','lat'])
#plt.figure()
ax1.axis([-71.05,-69.8,41.25,42.35])
for a in np.arange(len(num1)):
    ax1.scatter(lon1[a],lat1[a],s=num1[a]*3,color='red')
#plt.plot(coast_lon,coast_lat,'b.')
ax1.plot(CL['lon'],CL['lat'])

ax1.text(lon1[0],lat1[0],towns1[0])
ax1.text(lon1[1],lat1[1],towns1[1])
ax1.text(lon1[2],lat1[2],towns1[2])
ax1.text(lon1[3],lat1[3],towns1[3])
ax1.text(lon1[4],lat1[4],towns1[4])
ax1.text(lon1[5],lat1[5],towns1[5])
ax1.text(lon1[6]-0.1,lat1[6]-0.02,towns1[6])
ax1.text(lon1[7],lat1[7]-0.04,towns1[7])
ax1.text(lon1[8],lat1[8],towns1[8])
ax1.text(lon1[9],lat1[9],towns1[9])
#ax1.text(lon1[10]+0.04,lat1[10]+0.01,towns1[10])

ax1.set_title('strandings_1991_town')
ax1.set_xlabel('lon')
ax1.set_ylabel('lat')
#----------------second
ax2=fig.add_subplot(3,2,2)
c2 = np.genfromtxt('strandings_1992_only_town.csv',dtype=None,names=['turtle_ID','date','town'],delimiter=',',skip_header=1)
c2['town']=np.char.capitalize(c2['town'])
towns2=[]
for a in c2['town']:
    print a
    if a not in towns2:
        towns2.append(a)
num2=[]
for a in np.arange(len(towns2)):
    j=0
    for b in np.arange(len(c2['town'])):
        if towns2[a]==c2['town'][b]:
            j=j+1
    num2.append(j)
            
    #towns2[a]
lon2=[-70.3625,-70.0455,-70.1905,-70.6717,-70.1506,-69.9989,-70.5342,-70.0172,-70.4508,-70.0783,-70.0678,-70.5456]
lat2=[41.7251,41.7512,41.7411,42.0083,41.7511,41.7996,41.8342,41.785,41.7506,41.9583,41.9172,41.4125]
#FNCL='necscoast_worldvec.dat'
# lon lat pairs
# segments separated by nans

#CL=np.genfromtxt(FNCL,names=['lon','lat'])
#plt.figure()
ax2.axis([-71.05,-69.8,41.25,42.35])
for a in np.arange(len(num2)):
    ax2.scatter(lon2[a],lat2[a],s=num2[a]*3,color='red')
#plt.plot(coast_lon,coast_lat,'b.')
ax2.plot(CL['lon'],CL['lat'])

ax2.text(lon2[0],lat2[0]-0.03,towns2[0])
ax2.text(lon2[1],lat2[1],towns2[1])
ax2.text(lon2[2],lat2[2],towns2[2])
ax2.text(lon2[3],lat2[3],towns2[3])
ax2.text(lon2[4],lat2[4]-0.05,towns2[4])
ax2.text(lon2[5],lat2[5],towns2[5])
ax2.text(lon2[6],lat2[6],towns2[6])
ax2.text(lon2[7]-0.1,lat2[7],towns2[7])
ax2.text(lon2[8],lat2[8],towns2[8])
ax2.text(lon2[9],lat2[9],towns2[9])
ax2.text(lon2[10],lat2[10],towns2[10])
ax2.text(lon2[11],lat2[11],towns2[11])
#ax2.text(lon2[12],lat2[12],towns2[12])

ax2.set_title('strandings_1992_town')
ax2.set_xlabel('lon')
ax2.set_ylabel('lat')
#---------------third
ax3=fig.add_subplot(3,2,3)
c3 = np.genfromtxt('strandings_1999_only_town.csv',dtype=None,names=['turtle_ID','date','town'],delimiter=',',skip_header=1)
c3['town']=np.char.capitalize(c3['town'])
towns3=[]
for a in c3['town']:
    print a
    if a not in towns3:
        towns3.append(a)
num3=[]
for a in np.arange(len(towns3)):
    j=0
    for b in np.arange(len(c3['town'])):
        if towns3[a]==c3['town'][b]:
            j=j+1
    num3.append(j)
            
    #towns3[a]
lon3=[-70.3625,-70.5566,-70.0455,-69.9955,-70.9705,-70.1905,-70.1620,-69.9989,-69.9761,-70.1786,-70.0867,-70.0453,-70.5456]
lat3=[41.7251,41.7704,41.7512,41.6673,41.6130,41.7411,41.7426,41.7996,41.7859,42.0584,42.0376,41.8959,41.4125]

# lon lat pairs
# segments separated by nans

#CL=np.genfromtxt(FNCL,names=['lon','lat'])
#plt.figure()
ax3.axis([-71.05,-69.8,41.25,42.35])
for a in np.arange(len(num3)):
    ax3.scatter(lon3[a],lat3[a],s=num3[a]*3,color='red')
#plt.plot(coast_lon,coast_lat,'b.')
ax3.plot(CL['lon'],CL['lat'])

ax3.text(lon3[0],lat3[0],towns3[0])
ax3.text(lon3[1],lat3[1],towns3[1])
ax3.text(lon3[2]-0.1,lat3[2]+0.04,towns3[2])
ax3.text(lon3[3],lat3[3],towns3[3])
ax3.text(lon3[4],lat3[4],towns3[4])
ax3.text(lon3[5],lat3[5],towns3[5])
ax3.text(lon3[6],lat3[6]-0.04,towns3[6])
ax3.text(lon3[7],lat3[7],towns3[7])
ax3.text(lon3[8],lat3[8]-0.02,towns3[8])
ax3.text(lon3[9],lat3[9]+0.03,towns3[9])
ax3.text(lon3[10],lat3[10],towns3[10])
ax3.text(lon3[11],lat3[11],towns3[11])
ax3.text(lon3[12],lat3[12],towns3[12])

ax3.set_title('strandings_1999_town')
ax3.set_xlabel('lon')
ax3.set_ylabel('lat')
#---------------fourth
ax4=fig.add_subplot(3,2,4,)
c4 = np.genfromtxt('strandings_2001_only_town.csv',dtype=None,names=['turtle_ID','date','town'],delimiter=',',skip_header=1)
c4['town']=np.char.capitalize(c4['town'])
towns4=[]
for a in c4['town']:
    print a
    if a not in towns4:
        towns4.append(a)
num4=[]
for a in np.arange(len(towns4)):
    j=0
    for b in np.arange(len(c4['town'])):
        if towns4[a]==c4['town'][b]:
            j=j+1
    num4.append(j)
            
    #towns4[a]
lon4=[-70.3625,-70.0455,-70.1905,-69.9989,-69.9761,-70.0867,-70.0453,-70.2588]
lat4=[41.7251,41.7512,41.7411,41.7996,41.7859,42.0376,41.8959,41.7081]
#FNCL='necscoast_worldvec.dat'
# lon lat pairs
# segments separated by nans

#CL=np.genfromtxt(FNCL,names=['lon','lat'])
#plt.figure()
ax4.axis([-71.05,-69.8,41.25,42.35])
for a in np.arange(len(num4)):
    ax4.scatter(lon4[a],lat4[a],s=num4[a]*3,color='red')
#plt.plot(coast_lon,coast_lat,'b.')
ax4.plot(CL['lon'],CL['lat'])

ax4.text(lon4[0],lat4[0],towns4[0])
ax4.text(lon4[1],lat4[1]-0.03,towns4[1])
ax4.text(lon4[2],lat4[2],towns4[2])
ax4.text(lon4[3],lat4[3],towns4[3])
ax4.text(lon4[4],lat4[4]-0.02,towns4[4])
ax4.text(lon4[5],lat4[5],towns4[5])
ax4.text(lon4[6],lat4[6],towns4[6])
ax4.text(lon4[7],lat4[7]-0.03,towns4[7])

ax4.set_title('strandings_2001_town')
ax4.set_xlabel('lon')
ax4.set_ylabel('lat')
#-------------------fifth
ax5=fig.add_subplot(3,2,5)
c5 = np.genfromtxt('strandings_2002_only_town.csv',dtype=None,names=['turtle_ID','date','town'],delimiter=',',skip_header=1)
c5['town']=np.char.capitalize(c5['town'])
towns5=[]
for a in c5['town']:
    print a
    if a not in towns5:
        towns5.append(a)
num5=[]
for a in np.arange(len(towns5)):
    j=0
    for b in np.arange(len(c5['town'])):
        if towns5[a]==c5['town'][b]:
            j=j+1
    num5.append(j)
            
    #towns5[a]
lon5=[-70.3625,-70.0455,-70.1905,-69.9989,-69.9761,-70.1786,-70.0867,-70.0453,-70.2588,-70.5456]
lat5=[41.7251,41.7512,41.7411,41.7996,41.7859,42.0584,42.0376,41.8959,41.7081,41.4125]
#FNCL='necscoast_worldvec.dat'
# lon lat pairs
# segments separated by nans

#CL=np.genfromtxt(FNCL,names=['lon','lat'])
#plt.figure()
ax5.axis([-71.05,-69.8,41.25,42.35])
for a in np.arange(len(num5)):
    ax5.scatter(lon5[a],lat5[a],s=num5[a]*3,color='red')
#plt.plot(coast_lon,coast_lat,'b.')
ax5.plot(CL['lon'],CL['lat'])


ax5.text(lon5[0]-0.05,lat5[0]+0.02,towns5[0])
ax5.text(lon5[1]-0.05,lat5[1]-0.03,towns5[1])
ax5.text(lon5[2],lat5[2],towns5[2])
ax5.text(lon5[3],lat5[3],towns5[3])
ax5.text(lon5[4],lat5[4]-0.03,towns5[4])
ax5.text(lon5[5]-0.1,lat5[5]+0.03,towns5[5])
ax5.text(lon5[6],lat5[6],towns5[6])
ax5.text(lon5[7],lat5[7],towns5[7])
ax5.text(lon5[8]-0.05,lat5[8]-0.03,towns5[8])
ax5.text(lon5[9],lat5[9],towns5[9])
"""
ax5.text(lon5[10],lat5[10],towns5[10])
ax5.text(lon5[11],lat5[11],towns5[11])
ax5.text(lon5[12]-0.06,lat5[12]+0.02,towns5[12])
ax5.text(lon5[13],lat5[13],towns5[13])
ax5.text(lon5[14],lat5[14],towns5[14])
ax5.text(lon5[15],lat5[15],towns5[15])
ax5.text(lon5[16],lat5[16],towns5[16])
ax5.text(lon5[17],lat5[17]-0.05,towns5[17])
ax5.text(lon5[18],lat5[18],towns5[18])
"""
ax5.set_title('strandings_2002_town')
ax5.set_xlabel('lon')
ax5.set_ylabel('lat')
#--------------------sixth
ax6=fig.add_subplot(3,2,6)
c6 = np.genfromtxt('strandings_2003_only_town.csv',dtype=None,names=['turtle_ID','date','town'],delimiter=',',skip_header=1)
c6['town']=np.char.capitalize(c6['town'])
towns6=[]
for a in c6['town']:
    print a
    if a not in towns6:
        towns6.append(a)
num6=[]
for a in np.arange(len(towns6)):
    j=0
    for b in np.arange(len(c6['town'])):
        if towns6[a]==c6['town'][b]:
            j=j+1
    num6.append(j)
            
    #towns6[a]
lon6=[-70.3625,-70.0455,-70.1905,-69.9989,-69.9761,-70.5451,-70.1786,-70.4953,-70.0867,-70.0453,-70.2588]
lat6=[41.7251,41.7512,41.7411,41.7996,41.7859,41.8109,42.0584,41.7682,42.0376,41.8959,41.7081]
#FNCL='necscoast_worldvec.dat'
# lon lat pairs
# segments separated by nans

#CL=np.genfromtxt(FNCL,names=['lon','lat'])
#plt.figure()
ax6.axis([-71.05,-69.8,41.25,42.35])
for a in np.arange(len(num6)):
    ax6.scatter(lon6[a],lat6[a],s=num6[a]*3,color='red')
#plt.plot(coast_lon,coast_lat,'b.')
ax6.plot(CL['lon'],CL['lat'])

ax6.text(lon6[0],lat6[0],towns6[0])
ax6.text(lon6[1]-0.05,lat6[1]-0.03,towns6[1])
ax6.text(lon6[2],lat6[2],towns6[2])
ax6.text(lon6[3],lat6[3],towns6[3])
ax6.text(lon6[4],lat6[4]-0.03,towns6[4])
ax6.text(lon6[5],lat6[5],towns6[5])
ax6.text(lon6[6]-0.1,lat6[6]+0.03,towns6[6])
ax6.text(lon6[7],lat6[7],towns6[7])
ax6.text(lon6[8],lat6[8],towns6[8])
ax6.text(lon6[9],lat6[9],towns6[9])
ax6.text(lon6[10]-0.1,lat6[10]-0.05,towns6[10])
"""
ax6.text(lon6[11]-0.06,lat6[11]+0.03,towns6[11])
ax6.text(lon6[12],lat6[12],towns6[12])
ax6.text(lon6[13],lat6[13],towns6[13])
ax6.text(lon[14],lat[14],towns6[14])
ax6.text(lon[15],lat[15],towns6[15])
ax6.text(lon[16],lat[16],towns6[16])
ax6.text(lon[17],lat[17],towns6[17])
ax6.text(lon[18],lat[18],towns6[18])
"""
ax6.set_title('strandings_2003_town')
ax6.set_xlabel('lon')
ax6.set_ylabel('lat')
#plt.title('strandings_2012_town')
plt.savefig('strandings_1991-2003_town',dpi=100)
