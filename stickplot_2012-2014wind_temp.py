# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 11:29:29 2017

@author: huimin
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 23:55:13 2017
@author: xiaojian
just change name from plt1.py
"""
import numpy as np
import datetime as dt
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as AA
from scipy import  interpolate
from mpl_toolkits.axes_grid1 import host_subplot
import csv
tuttle_time_num_u2012=np.load('tuttle_time_num_u2012.npy')
tuttle_time_num_u2013=np.load('tuttle_time_u2013.npy')
tuttle_time_num_u2014=np.load('tuttle_time_u2014.npy')
tuttle_time_num_v2012=np.load('tuttle_time_num_v2012.npy')
tuttle_time_num_v2013=np.load('tuttle_time_v2013.npy')
tuttle_time_num_v2014=np.load('tuttle_time_v2014.npy')


tuttle_time_u2012=np.load('tuttle_time_u2012.npy')
tuttle_time_u2013=np.load('tuttle_time_num_u2013.npy')
tuttle_time_u2014=np.load('tuttle_time_num_u2014.npy')
tuttle_time_v2012=np.load('tuttle_time_v2012.npy')
tuttle_time_v2013=np.load('tuttle_time_num_v2013.npy')
tuttle_time_v2014=np.load('tuttle_time_num_v2014.npy')

wind_time_u2012=np.load('wind_time_u2012.npy')
wind_time_u2013=np.load('wind_time_u2013.npy')
wind_time_u2014=np.load('wind_time_u2014.npy')
wind_time_v2012=np.load('wind_time_v2012.npy')
wind_time_v2013=np.load('wind_time_v2013.npy')
wind_time_v2014=np.load('wind_time_v2014.npy')

wind_u2012=np.load('wind_u2012.npy')
wind_u2013=np.load('wind_u2013.npy')
wind_u2014=np.load('wind_u2014.npy')
wind_v2012=np.load('wind_v2012.npy')
wind_v2013=np.load('wind_v2013.npy')
wind_v2014=np.load('wind_v2014.npy')
t0=[datetime(2012,11,1,0)]
t0m=[]
t1=[datetime(2013,11,1,0)]
t1m=[]
t2=[datetime(2014,11,1,0)]
t2m=[]
for a in np.arange(20):
    t0.append(t0[0]+timedelta(days=3)*(a+1))
    t1.append(t1[0]+timedelta(days=3)*(a+1))
    t2.append(t2[0]+timedelta(days=3)*(a+1))
for a in np.arange(len(t0)-1):
    t0m.append(t0[a]+timedelta(days=1.5))
    t1m.append(t1[a]+timedelta(days=1.5))
    t2m.append(t2[a]+timedelta(days=1.5))
u2012=[]
wu2012=[]
wv2012=[]
for a in np.arange(len(t0)-1):
    print a
    s=0
    x=0
    w=0
    for b in np.arange(len(tuttle_time_u2012)):
        if tuttle_time_u2012[b]>=t0[a] and tuttle_time_u2012[b]<t0[a+1]:
            s=s+tuttle_time_num_u2012[b]
    for c in np.arange(len(wind_time_u2012)):
        if wind_time_u2012[c]>=t0[a] and wind_time_u2012[c]<t0[a+1]:
            w=w+wind_u2012[c]
            x=x+1
    u2012.append(s)
    wu2012.append(w/float(x))
v2012=[]
for a in np.arange(len(t0)-1):
    print a
    s=0
    x=0
    w=0
    for b in np.arange(len(tuttle_time_v2012)):
        if tuttle_time_v2012[b]>=t0[a] and tuttle_time_v2012[b]<t0[a+1]:
            s=s+tuttle_time_num_v2012[b]
    for c in np.arange(len(wind_time_v2012)):
        if wind_time_v2012[c]>=t0[a] and wind_time_v2012[c]<t0[a+1]:
            w=w+wind_v2012[c]
            x=x+1
    wv2012.append(w/float(x))
    v2012.append(s)
u2013=[]
wu2013=[]
wv2013=[]
for a in np.arange(len(t0)-1):
    print a
    s=0
    x=0
    w=0
    for b in np.arange(len(tuttle_time_u2013)):
        if tuttle_time_u2013[b]>=t1[a] and tuttle_time_u2013[b]<t1[a+1]:
            s=s+tuttle_time_num_u2013[b]
    for c in np.arange(len(wind_time_u2013)):
        if wind_time_u2013[c]>=t1[a] and wind_time_u2013[c]<t1[a+1]:
            w=w+wind_u2013[c]
            x=x+1
    u2013.append(s)
    wu2013.append(w/float(x))
    #u2013.append(s)
v2013=[]
for a in np.arange(len(t0)-1):
    print a
    s=0
    x=0
    w=0
    for b in np.arange(len(tuttle_time_v2013)):
        if tuttle_time_v2013[b]>=t1[a] and tuttle_time_v2013[b]<t1[a+1]:
            s=s+tuttle_time_num_v2013[b]
    for c in np.arange(len(wind_time_v2013)):
        if wind_time_v2013[c]>=t1[a] and wind_time_v2013[c]<t1[a+1]:
            w=w+wind_v2013[c]
            x=x+1
    wv2013.append(w/float(x))
    #v2012.append(s)
    v2013.append(s)
u2014=[]
wu2014=[]
wv2014=[]
for a in np.arange(len(t0)-1):
    print a
    s=0
    x=0
    w=0
    for b in np.arange(len(tuttle_time_u2014)):
        if tuttle_time_u2014[b]>=t2[a] and tuttle_time_u2014[b]<t2[a+1]:
            s=s+tuttle_time_num_u2014[b]
    for c in np.arange(len(wind_time_u2014)):
        if wind_time_u2014[c]>=t2[a] and wind_time_u2014[c]<t2[a+1]:
            w=w+wind_u2014[c]
            x=x+1
    u2014.append(s)
    wu2014.append(w/float(x))
    #u2014.append(s)
v2014=[]
for a in np.arange(len(t0)-1):
    print a
    s=0
    x=0
    w=0
    for b in np.arange(len(tuttle_time_v2014)):
        if tuttle_time_v2014[b]>=t2[a] and tuttle_time_v2014[b]<t2[a+1]:
            s=s+tuttle_time_num_v2014[b]
    for c in np.arange(len(wind_time_v2014)):
        if wind_time_v2014[c]>=t2[a] and wind_time_v2014[c]<t2[a+1]:
            w=w+wind_v2014[c]
            x=x+1
    wv2014.append(w/float(x))
    #v2012.append(s)
    #v2013.append(s)
    v2014.append(s)

fig,axes=plt.subplots(3,1,figsize=(12,10))
plt.subplots_adjust(wspace=0.4,hspace=0.4)
##########################################################

"""
s2012=[]
s2012.append(u2012)
s2012.append(v2012)
index1=[]
for a in np.arange(len(t0m)):
    index1.append("%s/%s"%(t0m[a].month,t0m[a].day))
d0=pd.DataFrame(np.array(s2012).T,index=index1,columns=pd.Index(['Outer Cape','Mid Cape']))
d0.plot(kind='bar',ax=axes[0])
for a in np.arange(len(t0m)):
    axes[0].arrow(a,60,wu2012[a],wv2012[a])
"""
t00=datetime(2004,3,31,0,0,0)#2004,
width1=t00=datetime(2004,4,1,0,0,0)-datetime(2004,3,31,0,0,0)
xz=[1,2,3,4,5,6,7,8,9]
axes[0].bar(t0m,u2012,width=1.2,label='Outer Cape')
axes[0].bar(np.array(t0m)+width1,v2012,width=1.2,label='Mid Cape')
for a in np.arange(len(t0m)):
    axes[0].arrow(t0m[a],60,timedelta(days=wu2012[a]*100).days,wv2012[a]*600,head_width=0.5)
axes[0].arrow(t0m[0],20,timedelta(days=wu2012[3]*100).days,wv2012[0]*600,head_width=0.5)
axes[0].plot([t0m[0],t0m[0]+timedelta(days=wu2012[3]*70)],[20,20])
axes[0].plot([t0m[0],t0m[0]],[20,20+wv2012[0]*600])
axes[0].text(t0m[0],30,'%spa'%(wu2012[3]))
axes[0].text(t0m[0]-timedelta(days=wu2012[3]*70),-10,'%spa'%(wv2012[0]))

axes[0].set_title('2012')
axes[0].set_ylim([-50,120])
axes[0].legend()

axes[1].bar(t1m,u2013,width=1.2,label='Outer Cape')
axes[1].bar(np.array(t1m)+width1,v2013,width=1.2,label='Mid Cape')
for a in np.arange(len(t0m)):
    axes[1].arrow(t1m[a],60,timedelta(days=wu2013[a]*100).days,wv2013[a]*600,head_width=0.5)
#axes[1].arrow(t1m[0],20,timedelta(days=wu2013[3]*100).days,wv2013[0]*600,head_width=0.5)
axes[1].set_ylim([-50,120])
axes[1].legend()
axes[1].set_title('2013')

axes[2].bar(t2m,u2014,width=1.2,label='Outer Cape')
axes[2].bar(np.array(t2m)+width1,v2014,width=1.2,label='Mid Cape')
for a in np.arange(len(t2m)):
    axes[2].arrow(t2m[a],500,timedelta(days=wu2014[a]*100).days,wv2014[a]*600,head_width=0.5)
axes[2].set_ylim([-50,700])
axes[2].legend()
axes[2].set_title('2014')
plt.savefig('wind_strandings',dpi=300)