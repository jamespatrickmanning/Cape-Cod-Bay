# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 01:05:39 2017

@author: xiaojian
"""
import numpy as np
import matplotlib.pyplot as plt

f = np.genfromtxt('eMOLT_2012_2016_CCBay.csv',dtype=None,names=['s','t','lat','lon','deep','tem'],delimiter=',',skip_header=1)  
n=[0]
for a in np.arange(len(f['s'])-1):
    if f['s'][a]!=f['s'][a+1]:
        n.append(a+1)
n.append(len(f)-1)

fig,axes=plt.subplots(1,1,figsize=(10,8))
FNCL='necscoast_worldvec.dat'

CL=np.genfromtxt(FNCL,names=['lon','lat'])
axes.axis([-71.,-69.8,41.5,42.7])
XXX=0
for a in np.arange(len(n)-1):
    if f['s'][n[a]]=='RM03' or f['s'][n[a]]=='BS02':
        pass
    elif f['s'][n[a]]=='AB01':
        axes.scatter(f['lon'][n[a]],f['lat'][n[a]],s=40,color='red')
        axes.text(f['lon'][n[a]]-0.01,f['lat'][n[a]]+0.04,f['s'][n[a]],fontsize=13)
    elif f['s'][n[a]][:-1]=='DMF' and f['s'][n[a]]!='DMF4':
        XXX=a
        axes.scatter(f['lon'][n[a]],f['lat'][n[a]],s=40,marker='s',color='g')
        axes.text(f['lon'][n[a]]-0.01,f['lat'][n[a]]+0.01,f['s'][n[a]],fontsize=13)
    elif f['s'][n[a]]=='DMF4':
        
        axes.scatter(f['lon'][n[a]],f['lat'][n[a]],s=40,marker='s',color='g')
        axes.text(f['lon'][n[a]]+0.02,f['lat'][n[a]]-0.01,f['s'][n[a]],fontsize=13)
    else:
        axes.scatter(f['lon'][n[a]],f['lat'][n[a]],s=40,color='red')
        axes.text(f['lon'][n[a]]-0.01,f['lat'][n[a]]+0.01,f['s'][n[a]],fontsize=13)
axes.scatter(f['lon'][n[a]],f['lat'][n[a]],s=40,color='red',label='eMOLT')
axes.scatter(f['lon'][n[XXX]],f['lat'][n[XXX]],s=40,marker='s',color='g',label='DMF')

haa=[-70.566,42.52283]
axes.scatter(haa[0],haa[1],s=40,marker='^',color='b',label='NERACOOS')
axes.text(haa[0]+0.02,haa[1],'Mooring A',fontsize=13)
axes.scatter(-70.32,41.83,s=40,marker='^',color='b')
axes.text(-70.32+0.01,41.83-0.01,'CDIP',fontsize=13)
axes.plot(CL['lon'],CL['lat'],linewidth=1)
#axes.xaxis.tick_top() 
for tick in axes.yaxis.get_major_ticks():  
    tick.label1.set_fontsize(13)
for tick in axes.xaxis.get_major_ticks():  
    tick.label1.set_fontsize(13)
plt.legend(fontsize=13,scatterpoints=1)
plt.savefig('emolt2x',dpi=200,bbox_inches = "tight")
plt.savefig('emolt2x.ps',dpi=200,bbox_inches = "tight")
plt.show()
