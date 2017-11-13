# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 10:59:05 2017

@author: huimin
"""
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import pytz
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from pytz import timezone
import numpy as np
import csv
from scipy import  interpolate
from matplotlib.dates import date2num,num2date

FNCL='necscoast_worldvec.dat'
CL=np.genfromtxt(FNCL,names=['lon','lat'])

fig=plt.figure(figsize=(20,8))
axes1=fig.add_subplot(1,2,1)
axes2=fig.add_subplot(1,2,2)

lon1=np.linspace(-70.45,-70.2,10)
lat1=np.linspace(42.05,41.8,10)
axes1.plot(CL['lon'],CL['lat'])
axes1.axis([-70.94,-70.0,41.52659,42.562711])
axes1.scatter(lon1,lat1,color='red',s=7)



# lon lat pairs
# segments separated by nans

label=['A','B','C','D','E','F','G','H','I','J']
dian=['a','b','c','d','e','f','g','h','i','j']


for a in np.arange(len(label)):
    axes1.text(lon1[a]-0.05,lat1[a]-0.03,label[a],fontsize=12)

#axes2.axis([-70.75,-69.8,41.5,42.23])


#lat=np.linspace(41.8,42.4,10)
#lon=np.linspace(-70.15,-70.75,10)
axes2.plot(CL['lon'],CL['lat'])
#axes3.axis([-70.94,-70.0,41.52659,42.562711])
#axes2.scatter(lon,lat,s=7,color='red')
lat=np.linspace(41.8,42.4,10)
lon=np.linspace(-70.15,-70.75,10)
axes2.axis([-70.94,-70.0,41.52659,42.562711])
axes2.scatter(lon,lat,color='red',s=7)

for a in np.arange(len(lon)):
    axes2.text(lon[a]-0.05,lat[a],dian[a],fontsize=12)
#axes2.xaxis.tick_top() 
axes1.xaxis.tick_top() 
axes2.xaxis.tick_top()
axes1.set_xlabel('a',fontsize=12)
axes2.set_xlabel('b',fontsize=12)
plt.savefig('points_wind&temp',dpi=400)