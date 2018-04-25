# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 09:17:24 2016

@author: xiaojian
"""
import datetime as dt
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np
import csv
drifter_list='nearest.csv'
mend_list='bar.csv'
drifters = np.genfromtxt(drifter_list,dtype=None,names=['ids','meandis','mindis','maxdis','meandisdis','mindisdis','maxdisdis'],delimiter=',',skip_header=1)
mend = np.genfromtxt(mend_list,dtype=None,names=['ids','meandis','mindis','maxdis','meandisdis','mindisdis','maxdisdis'],delimiter=',',skip_header=1)   

plt.figure()
plt.title('drifter_meandis_and_mend_meandis') 
plt.plot(drifters['meandis'],'bo-')
plt.plot(mend['meandis'],'ro-')
plt.savefig('drifter_meandis_and_mend_meandis')
plt.show()

plt.figure()
plt.title('drifter_mindis_and_mend_mindis') 
plt.plot(drifters['mindis'],'bo-')
plt.plot(mend['mindis'],'ro-')
plt.savefig('drifter_mindis_and_mend_mindis')
plt.show()

plt.figure()
plt.title('drifter_maxdis_and_mend_maxdis') 
plt.plot(drifters['maxdis'],'bo-')
plt.plot(mend['maxdis'],'ro-')
plt.savefig('drifter_maxdis_and_mend_maxdis')
plt.show()

plt.figure()
plt.title('drifter_meandisdis_and_mend_meandisdis') 
plt.plot(drifters['meandisdis'],'bo-')
plt.plot(mend['meandisdis'],'ro-')
plt.savefig('drifter_meandisdis_and_mend_meandisdis')
plt.show()

plt.figure()
plt.title('drifter_mindisdis_and_mend_mindisdis') 
plt.plot(drifters['mindisdis'],'bo-')
plt.plot(mend['mindisdis'],'ro-')
plt.savefig('drifter_mindisdis_and_mend_mindisdis')
plt.show()

plt.figure()
plt.title('drifter_maxdisdis_and_mend_maxdisdis') 
plt.plot(drifters['maxdisdis'],'bo-')
plt.plot(mend['maxdisdis'],'ro-')
plt.savefig('drifter_maxdisdis_and_mend_maxdisdis')
plt.show()
di=[]

for a in np.arange(len(drifters['ids'])):
    di.append(0)
df=drifters['meandis']-mend['meandis']
maxx=drifters['meandis']-mend['meandis']
minn=drifters['meandis']-mend['meandis']
i=0
j=0
for b in np.arange(len(drifters['ids'])):
    if maxx[b]<0:
        maxx[b]=0
    else:
        i=i+1
    if minn[b]>=0:
        minn[b]=0
    else:
        j=j+1    
plt.figure()
plt.title('drifter_meandis_and_mend_meandis_different') 
plt.plot(maxx,'ro-',label='red_point_num=%s'%(i))
plt.plot(minn,'bo-',label='blue_point_num=%s'%(j))
plt.legend()
plt.plot(di,'g*-')
plt.savefig('drifter_meandis_and_mend_meandis_different')
plt.show()

mend_mean=np.mean(mend['meandis'])
drifters_mean=np.mean(drifters['meandis'])
m_std=mend['meandis'].std()   
d_std=drifters['meandis'].std()
print 'mend_meandis',mend_mean,'drifters_meandis',drifters_mean
print 'mend_std',m_std,'drifters_std',d_std
i
h1=[]
h2=[]
hm=[]
hs=[]
r1=[]
h1.append(drifters_mean)
h1.append(mend_mean)
hm.append(h1)
h2.append(d_std)
h2.append(m_std)
hs.append(h2)
r1.append(drifters_mean)
r1.append(d_std)
r2=[]
r2.append(mend_mean)
r2.append(m_std)
r=[]
z1=[]
z2=[]
z1.append(drifters_mean)
z1.append(mend_mean)
z2.append(d_std)
z2.append(m_std)
r.append(r1)
r.append(r2)
a=i/float(i+j)
print a


#csvfile = file('drifter_vs_model use hourly data.csv', 'wb')
'''
csvfile = file('drifter_and_mend.csv', 'wb')
writer = csv.writer(csvfile)
f=['aa']
for z in range(1):
    f.append('mean')
    f.append('std')
chat=map(list, zip(*f))
writer.writerows(chat)
row1=['before']
row2=['mend']
row1.append(drifters_mean)
row1.append(d_std)
row2.append(mend_mean)
row2.append(m_std)
chat1=map(list, zip(*row1))
writer.writerows(chat1)
chat2=map(list, zip(*row2))
writer.writerows(chat1)
writer.writerows(chat2)

csvfile.close()
'''

di=[]

for a in np.arange(len(drifters['ids'])):
    di.append(0)
df=drifters['mindis']-mend['mindis']
maxx=drifters['mindis']-mend['mindis']
minn=drifters['mindis']-mend['mindis']
i=0
j=0
for b in np.arange(len(drifters['ids'])):
    if maxx[b]<0:
        maxx[b]=0
    else:
        i=i+1
    if minn[b]>=0:
        minn[b]=0
    else:
        j=j+1    
plt.figure()
plt.title('drifter_mindis_and_mend_mindis_different') 
plt.plot(maxx,'ro-',label='red_point_num=%s'%(i))
plt.plot(minn,'bo-',label='blue_point_num=%s'%(j))
plt.legend()
plt.plot(di,'g*-')
plt.savefig('drifter_mindis_and_mend_mindis_different')
plt.show()

mend_mean=np.mean(mend['mindis'])
drifters_mean=np.mean(drifters['mindis'])
m_std=mend['mindis'].std()   
d_std=drifters['mindis'].std()
print 'mend_mindis',mend_mean,'drifters_mindis',drifters_mean
print 'mend_std',m_std,'drifters_std',d_std
i
h1=[]
h2=[]
h1.append(drifters_mean)
h1.append(mend_mean)
h2.append(d_std)
h2.append(m_std)
hm.append(h1)
hs.append(h2)
r1=[]
r1.append(drifters_mean)
r1.append(d_std)
r2=[]
r2.append(mend_mean)
r2.append(m_std)
z1.append(drifters_mean)
z1.append(mend_mean)
z2.append(d_std)
z2.append(m_std)
r.append(r1)
r.append(r2)
a=i/float(i+j)
print a


di=[]

for a in np.arange(len(drifters['ids'])):
    di.append(0)
df=drifters['maxdis']-mend['maxdis']
maxx=drifters['maxdis']-mend['maxdis']
minn=drifters['maxdis']-mend['maxdis']
i=0
j=0
for b in np.arange(len(drifters['ids'])):
    if maxx[b]<0:
        maxx[b]=0
    else:
        i=i+1
    if minn[b]>=0:
        minn[b]=0
    else:
        j=j+1    
plt.figure()
plt.title('drifter_mindis_and_mend_mindis_different') 
plt.plot(maxx,'ro-',label='red_point_num=%s'%(i))
plt.plot(minn,'bo-',label='blue_point_num=%s'%(j))
plt.legend()
plt.plot(di,'g*-')
plt.savefig('drifter_mindis_and_mend_mindis_different')
plt.show()

mend_mean=np.mean(mend['maxdis'])
drifters_mean=np.mean(drifters['maxdis'])
m_std=mend['maxdis'].std()   
d_std=drifters['maxdis'].std()
print 'mend_maxdis',mend_mean,'drifters_maxdis',drifters_mean
print 'mend_std',m_std,'drifters_std',d_std
i
h1=[]
h2=[]
h1.append(drifters_mean)
h1.append(mend_mean)
h2.append(d_std)
h2.append(m_std)
hm.append(h1)
hs.append(h2)
r1=[]
r1.append(drifters_mean)
r1.append(d_std)
r2=[]
r2.append(mend_mean)
r2.append(m_std)
z1.append(drifters_mean)
z1.append(mend_mean)
z2.append(d_std)
z2.append(m_std)
r.append(r1)
r.append(r2)
a=i/float(i+j)
print a


di=[]

for a in np.arange(len(drifters['ids'])):
    di.append(0)
df=drifters['meandisdis']-mend['meandisdis']
maxx=drifters['meandisdis']-mend['meandisdis']
minn=drifters['meandisdis']-mend['meandisdis']
i=0
j=0
for b in np.arange(len(drifters['ids'])):
    if maxx[b]<0:
        maxx[b]=0
    else:
        i=i+1
    if minn[b]>=0:
        minn[b]=0
    else:
        j=j+1    
plt.figure()
plt.title('drifter_meandisdis_and_mend_meandisdis_different') 
plt.plot(maxx,'ro-',label='red_point_num=%s'%(i))
plt.plot(minn,'bo-',label='blue_point_num=%s'%(j))
plt.legend()
plt.plot(di,'g*-')
plt.savefig('drifter_meandisdis_and_mend_meandisdis_different')
plt.show()
mend_mean=np.mean(mend['meandisdis'])
drifters_mean=np.mean(drifters['meandisdis'])
m_std=mend['meandisdis'].std()   
d_std=drifters['meandisdis'].std()
print 'mend_meandisdis',mend_mean,'drifters_meandisdis',drifters_mean
print 'mend_std',m_std,'drifters_std',d_std
i
h1=[]
h2=[]
h1.append(drifters_mean)
h1.append(mend_mean)
h2.append(d_std)
h2.append(m_std)
hm.append(h1)
hs.append(h2)
r1=[]
r1.append(drifters_mean)
r1.append(d_std)
r2=[]
r2.append(mend_mean)
r2.append(m_std)
z1.append(drifters_mean)
z1.append(mend_mean)
z2.append(d_std)
z2.append(m_std)
r.append(r1)
r.append(r2)
a=i/float(i+j)
print a


di=[]

for a in np.arange(len(drifters['ids'])):
    di.append(0)
df=drifters['mindisdis']-mend['mindisdis']
maxx=drifters['mindisdis']-mend['mindisdis']
minn=drifters['mindisdis']-mend['mindisdis']
i=0
j=0
for b in np.arange(len(drifters['ids'])):
    if maxx[b]<0:
        maxx[b]=0
    else:
        i=i+1
    if minn[b]>=0:
        minn[b]=0
    else:
        j=j+1    
plt.figure()
plt.title('drifter_mindisdis_and_mend_mindisdis_different') 
plt.plot(maxx,'ro-',label='red_point_num=%s'%(i))
plt.plot(minn,'bo-',label='blue_point_num=%s'%(j))
plt.legend()
plt.plot(di,'g*-')
plt.savefig('drifter_mindisdis_and_mend_mindisdis_different')
plt.show()

mend_mean=np.mean(mend['mindisdis'])
drifters_mean=np.mean(drifters['mindisdis'])
m_std=mend['mindisdis'].std()   
d_std=drifters['mindisdis'].std()
print 'mend_mindis',mend_mean,'drifters_mindis',drifters_mean
print 'mend_std',m_std,'drifters_std',d_std
i
h1=[]
h2=[]
h1.append(drifters_mean)
h1.append(mend_mean)
h2.append(d_std)
h2.append(m_std)
hm.append(h1)
hs.append(h2)
r1=[]
r1.append(drifters_mean)
r1.append(d_std)
r2=[]
r2.append(mend_mean)
r2.append(m_std)
z1.append(drifters_mean)
z1.append(mend_mean)
z2.append(d_std)
z2.append(m_std)
r.append(r1)
r.append(r2)
a=i/float(i+j)
print a



di=[]

for a in np.arange(len(drifters['ids'])):
    di.append(0)
df=drifters['maxdisdis']-mend['maxdisdis']
maxx=drifters['maxdisdis']-mend['maxdisdis']
minn=drifters['maxdisdis']-mend['maxdisdis']
i=0
j=0
for b in np.arange(len(drifters['ids'])):
    if maxx[b]<0:
        maxx[b]=0
    else:
        i=i+1
    if minn[b]>=0:
        minn[b]=0
    else:
        j=j+1    
plt.figure()
plt.title('drifter_maxdisdis_and_mend_maxdisdis_different') 
plt.plot(maxx,'ro-',label='red_point_num=%s'%(i))
plt.plot(minn,'bo-',label='blue_point_num=%s'%(j))
plt.legend()
plt.plot(di,'g*-')
plt.savefig('drifter_maxdisdis_and_mend_maxdisdis_different')
plt.show()

mend_mean=np.mean(mend['maxdisdis'])
drifters_mean=np.mean(drifters['maxdisdis'])
m_std=mend['maxdisdis'].std()   
d_std=drifters['maxdisdis'].std()
print 'mend_maxdisdis',mend_mean,'drifters_maxdisdis',drifters_mean
print 'mend_std',m_std,'drifters_std',d_std
i
h1=[]
h2=[]
h1.append(drifters_mean)
h1.append(mend_mean)
h2.append(d_std)
h2.append(m_std)
hm.append(h1)
hs.append(h2)
r1=[]
r1.append(drifters_mean)
r1.append(d_std)
r2=[]
r2.append(mend_mean)
r2.append(m_std)
z1.append(drifters_mean)
z1.append(mend_mean)
z2.append(d_std)
z2.append(m_std)
r.append(r1)
r.append(r2)
df1=pd.DataFrame(r,index=['before_meandis','mend_meandis','before_mindis','mend_mindis','before_maxdis','mend_maxdis','before_meandisdis','mend_meandisdis','before_mindisdis','mend_mindisdis','before_maxdisdis','mend_maxdisdis'],columns=pd.Index(['mean','std'],name='difference'))
df1.plot(kind='bar',stacked='True')
a=i/float(i+j)
print a
z1b=['before_meandis_mean','mend_meandis_mean','before_mindis_mean','mend_mindis_mean','before_maxdis_mean','mend_maxdis_mean','before_meandisdis_mean','mend_meandisdis_mean','before_mindisdis_mean','mend_mindisdis_mean','before_maxdisdis_mean','mend_maxdisdis_mean']
z2b=['before_meandis_std','mend_meandis_std','before_mindis_std','mend_mindis_std','before_maxdis_std','mend_maxdis_std','before_meandisdis_std','mend_meandisdis_std','before_mindisdis_std','mend_mindisdis_std','before_maxdisdis_std','mend_maxdisdis_std']
#dataj=[]
#dataj.append(z1b.T)
#dataj.append(z1.T)
#plt.figure()
df1=pd.DataFrame(z1,index=z1b)
df1.plot(kind='bar')#,stacked='True')

df1=pd.DataFrame(z2,index=z2b)
df1.plot(kind='bar')#,stacked='True')
df1=pd.DataFrame(hm,index=['meandis','mindis','maxdis','meandisdis','mindisdis','maxdisdis'],columns=pd.Index(['before','mend'],name='mean'))
df1.plot(kind='bar')#,stacked='True')

df1=pd.DataFrame(hs,index=['meandis','mindis','maxdis','meandisdis','mindisdis','maxdisdis'],columns=pd.Index(['before','mend'],name='std'))
df1.plot(kind='bar')











