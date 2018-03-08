# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 09:13:45 2017

@author: xiaojian
"""
import numpy as np
import matplotlib.pyplot as plt

date='NOV_18-25_2014'
m26=np.load('m_psFVCOM20141118_7days.npy')#'m_ps2011-2010_630.npy'
p=m26.tolist()
print len(p['lon'])
FN='necscoast_worldvec.dat'
CL=np.genfromtxt(FN,names=['lon','lat'])
fig,ax=plt.subplots(1,1,figsize=(8,8))#sharex=True,sharey=True,dpi=800,figsize=(15,15))
plt.subplots_adjust(wspace=0.1,hspace=0.1)

ax.plot(CL['lon'],CL['lat'],'b-')
for a in np.arange(len(p['lon'][0])):
    ax.scatter(p['lon'][0][a][0],p['lat'][0][a][0],color='green')
    if len(p['lon'][0][a])>=361: 
        print 'ooooooooooooooooooooooooooooooooooooooooooooooooooo '
        ax.scatter(p['lon'][0][a][360],p['lat'][0][a][360],color='red')
        ax.plot([p['lon'][0][a][0],p['lon'][0][a][360]],[p['lat'][0][a][0],p['lat'][0][a][360]],'y-')#,linewidth=0.5)
    else:
        ax.scatter(p['lon'][0][a][-1],p['lat'][0][a][-1],color='red')
        ax.plot([p['lon'][0][a][0],p['lon'][0][a][-1]],[p['lat'][0][a][0],p['lat'][0][a][-1]],'y-')#,linewidth=0.5)
        
ax.scatter(p['lon'][0][a][0],p['lat'][0][a][0],label='start',color='green')
ax.scatter(p['lon'][0][a][-1],p['lat'][0][a][-1],label='end',color='red')  

ax.legend()
ax.set_xlim([-70.7,-69.9])
ax.set_ylim([41.5,42.1])
ax.set_title('NOV 18-25 2014 surface particle trajectories',fontsize=14)
"""
axes[0,0].plot(CL['lon'],CL['lat'],'b-')
for a in np.arange(len(p['lon'][2])):
    axes[0,0].scatter(p['lon'][2][a][0],p['lat'][2][a][0],color='green')
    if len(p['lon'][2][a])>=361:
        
        axes[0,0].scatter(p['lon'][2][a][360],p['lat'][2][a][360],color='red')
        axes[0,0].plot([p['lon'][2][a][0],p['lon'][2][a][360]],[p['lat'][2][a][0],p['lat'][2][a][360]],'y-')#,linewidth=0.5)
    else:
        axes[0,0].scatter(p['lon'][2][a][-1],p['lat'][2][a][-1],color='red')
        axes[0,0].plot([p['lon'][2][a][0],p['lon'][2][a][-1]],[p['lat'][2][a][0],p['lat'][2][a][-1]],'y-')#,linewidth=0.5)
axes[0,0].scatter(p['lon'][2][a][0],p['lat'][2][a][0],label='start',color='green')
axes[0,0].scatter(p['lon'][2][a][-1],p['lat'][2][a][-1],label='end',color='red')
axes[0,0].plot(CL['lon'],CL['lat'],'b-',linewidth=0.5) 
axes[0,0].legend(loc='best') 
axes[0,0].set_xlabel('2007')
axes[0,0].set_xlim([-69.5,-65])
axes[0,0].set_ylim([43.4,45.6]) 
axes[0,0].xaxis.tick_top() 

axes[0,1].plot(CL['lon'],CL['lat'],'b-')
for a in np.arange(len(p['lon'][1])):
    axes[0,1].scatter(p['lon'][1][a][0],p['lat'][1][a][0],color='green')
    if len(p['lon'][1][a])>=361:
        
        axes[0,1].scatter(p['lon'][1][a][360],p['lat'][1][a][360],color='red')
        axes[0,1].plot([p['lon'][1][a][0],p['lon'][1][a][360]],[p['lat'][1][a][0],p['lat'][1][a][360]],'y-')#,linewidth=0.5)
    else:
        axes[0,1].scatter(p['lon'][1][a][-1],p['lat'][1][a][-1],color='red')
        axes[0,1].plot([p['lon'][1][a][0],p['lon'][1][a][-1]],[p['lat'][1][a][0],p['lat'][1][a][-1]],'y-')#,linewidth=0.5)
axes[0,1].scatter(p['lon'][1][a][0],p['lat'][1][a][0],label='start',color='green')
axes[0,1].scatter(p['lon'][1][a][-1],p['lat'][1][a][-1],label='end',color='red')
axes[0,1].plot(CL['lon'],CL['lat'],'b-',linewidth=0.5)
axes[0,1].set_xlabel('2008')
axes[0,1].xaxis.tick_top() 
axes[0,1].set_yticklabels([])
axes[0,1].set_xlim([-69.5,-65])
axes[0,1].set_ylim([43.4,45.6]) 
#plt.legend(loc='best') 


axes[0,2].plot(CL['lon'],CL['lat'],'b-')
for a in np.arange(len(p['lon'][0])):
    axes[0,2].scatter(p['lon'][0][a][0],p['lat'][0][a][0],color='green')
    if len(p['lon'][0][a])>=361:
        
        axes[0,2].scatter(p['lon'][0][a][360],p['lat'][0][a][360],color='red')
    #print len(lon[a])
        axes[0,2].plot([p['lon'][0][a][0],p['lon'][0][a][360]],[p['lat'][0][a][0],p['lat'][0][a][360]],'y-')#,linewidth=0.5)
    else:
        
        axes[0,2].scatter(p['lon'][0][a][-1],p['lat'][0][a][-1],color='red')
        axes[0,2].plot([p['lon'][0][a][0],p['lon'][0][a][-1]],[p['lat'][0][a][0],p['lat'][0][a][-1]],'y-')#,linewidth=0.5)
  
axes[0,2].scatter(p['lon'][0][a][0],p['lat'][0][a][0],label='start',color='green')
axes[0,2].scatter(p['lon'][0][a][-1],p['lat'][0][a][-1],label='end',color='red')  
axes[0,2].set_xlabel('2009')
axes[0,2].xaxis.tick_top() 

axes[0,2].set_yticklabels([])
axes[0,2].set_xlim([-70.5,-70.2])
axes[0,2].set_ylim([41.8,42.0]) 

m26=np.load('m_ps2011-2010_530.npy')#'m_ps2011-2010_630.npy'
p=m26.tolist()
axes[1,0].plot(CL['lon'],CL['lat'],'b-')
for a in np.arange(len(p['lon'][1])):
    axes[1,0].scatter(p['lon'][1][a][0],p['lat'][1][a][0],color='green')
    if len(p['lon'][1][a])>=361:
        
        axes[1,0].scatter(p['lon'][1][a][360],p['lat'][1][a][360],color='red')
        axes[1,0].plot([p['lon'][1][a][0],p['lon'][1][a][360]],[p['lat'][1][a][0],p['lat'][1][a][360]],'y-')#,linewidth=0.5)
    else:
        axes[1,0].scatter(p['lon'][1][a][-1],p['lat'][1][a][-1],color='red')
        axes[1,0].plot([p['lon'][1][a][0],p['lon'][1][a][-1]],[p['lat'][1][a][0],p['lat'][1][a][-1]],'y-')#,linewidth=0.5)
axes[1,0].scatter(p['lon'][1][a][0],p['lat'][1][a][0],label='start',color='green')
axes[1,0].scatter(p['lon'][1][a][-1],p['lat'][1][a][-1],label='end',color='red')
axes[1,0].plot(CL['lon'],CL['lat'],'b-',linewidth=0.5)
axes[1,0].set_xlabel('2010')
axes[1,0].set_xticklabels([])
#axes[0,1].set_xticklabels([])
axes[1,0].set_xlim([-69.5,-65])
axes[1,0].set_ylim([43.4,45.6]) 

axes[1,1].plot(CL['lon'],CL['lat'],'b-')
for a in np.arange(len(p['lon'][0])):
    axes[1,1].scatter(p['lon'][0][a][0],p['lat'][0][a][0],color='green')
    if len(p['lon'][0][a])>=361:
        
        axes[1,1].scatter(p['lon'][0][a][360],p['lat'][0][a][360],color='red')
    #print len(lon[a])
        axes[1,1].plot([p['lon'][0][a][0],p['lon'][0][a][360]],[p['lat'][0][a][0],p['lat'][0][a][360]],'y-')#,linewidth=0.5)
    else:
        
        axes[1,1].scatter(p['lon'][0][a][-1],p['lat'][0][a][-1],color='red')
        axes[1,1].plot([p['lon'][0][a][0],p['lon'][0][a][-1]],[p['lat'][0][a][0],p['lat'][0][a][-1]],'y-')#,linewidth=0.5)
  
axes[1,1].scatter(p['lon'][0][a][0],p['lat'][0][a][0],label='start',color='green')
axes[1,1].scatter(p['lon'][0][a][-1],p['lat'][0][a][-1],label='end',color='red')  
axes[1,1].set_xlabel('2011')
axes[1,1].set_yticklabels([])
axes[1,1].set_xticklabels([])
axes[1,1].set_xlim([-69.5,-65])
axes[1,1].set_ylim([43.4,45.6]) 



m26=np.load('m_ps2013-2012_530.npy')#'m_ps2011-2010_630.npy'
p=m26.tolist()
axes[1,2].plot(CL['lon'],CL['lat'],'b-')
for a in np.arange(len(p['lon'][1])):
    axes[1,2].scatter(p['lon'][1][a][0],p['lat'][1][a][0],color='green')
    if len(p['lon'][1][a])>=361:
        
        axes[1,2].scatter(p['lon'][1][a][360],p['lat'][1][a][360],color='red')
        axes[1,2].plot([p['lon'][1][a][0],p['lon'][1][a][360]],[p['lat'][1][a][0],p['lat'][1][a][360]],'y-')#,linewidth=0.5)
    else:
        axes[1,2].scatter(p['lon'][1][a][-1],p['lat'][1][a][-1],color='red')
        axes[1,2].plot([p['lon'][1][a][0],p['lon'][1][a][-1]],[p['lat'][1][a][0],p['lat'][1][a][-1]],'y-')#,linewidth=0.5)
axes[1,2].scatter(p['lon'][1][a][0],p['lat'][1][a][0],label='start',color='green')
axes[1,2].scatter(p['lon'][1][a][-1],p['lat'][1][a][-1],label='end',color='red')
axes[1,2].plot(CL['lon'],CL['lat'],'b-',linewidth=0.5)
axes[1,2].set_xlabel('2012')
axes[1,2].set_yticklabels([])
axes[1,2].set_xticklabels([])
axes[1,2].set_xlim([-69.5,-65])
axes[1,2].set_ylim([43.4,45.6]) 

axes[2,0].plot(CL['lon'],CL['lat'],'b-')
for a in np.arange(len(p['lon'][0])):
    axes[2,0].scatter(p['lon'][0][a][0],p['lat'][0][a][0],color='green')
    if len(p['lon'][0][a])>=361:
        
        axes[2,0].scatter(p['lon'][0][a][360],p['lat'][0][a][360],color='red')
    #print len(lon[a])
        axes[2,0].plot([p['lon'][0][a][0],p['lon'][0][a][360]],[p['lat'][0][a][0],p['lat'][0][a][360]],'y-')#,linewidth=0.5)
    else:
        
        axes[2,0].scatter(p['lon'][0][a][-1],p['lat'][0][a][-1],color='red')
        axes[2,0].plot([p['lon'][0][a][0],p['lon'][0][a][-1]],[p['lat'][0][a][0],p['lat'][0][a][-1]],'y-')#,linewidth=0.5)
  
axes[2,0].scatter(p['lon'][0][a][0],p['lat'][0][a][0],label='start',color='green')
axes[2,0].scatter(p['lon'][0][a][-1],p['lat'][0][a][-1],label='end',color='red')  
axes[2,0].set_xlabel('2013')
axes[2,0].set_xticklabels([])
axes[2,0].set_xlim([-69.5,-65])
axes[2,0].set_ylim([43.4,45.6]) 


m26=np.load('m_ps2015-2014_530.npy')#'m_ps2011-2010_630.npy'
p=m26.tolist()
axes[2,1].plot(CL['lon'],CL['lat'],'b-')
for a in np.arange(len(p['lon'][1])):
    axes[2,1].scatter(p['lon'][1][a][0],p['lat'][1][a][0],color='green')
    if len(p['lon'][1][a])>=361:
        
        axes[2,1].scatter(p['lon'][1][a][360],p['lat'][1][a][360],color='red')
        axes[2,1].plot([p['lon'][1][a][0],p['lon'][1][a][360]],[p['lat'][1][a][0],p['lat'][1][a][360]],'y-')#,linewidth=0.5)
    else:
        axes[2,1].scatter(p['lon'][1][a][-1],p['lat'][1][a][-1],color='red')
        axes[2,1].plot([p['lon'][1][a][0],p['lon'][1][a][-1]],[p['lat'][1][a][0],p['lat'][1][a][-1]],'y-')#,linewidth=0.5)
axes[2,1].scatter(p['lon'][1][a][0],p['lat'][1][a][0],label='start',color='green')
axes[2,1].scatter(p['lon'][1][a][-1],p['lat'][1][a][-1],label='end',color='red')
axes[2,1].plot(CL['lon'],CL['lat'],'b-',linewidth=0.5)
axes[2,1].set_xlabel('2014')
axes[2,1].set_yticklabels([])
axes[2,1].set_xticklabels([])
axes[2,1].set_xlim([-69.5,-65])
axes[2,1].set_ylim([43.4,45.6]) 

axes[2,2].plot(CL['lon'],CL['lat'],'b-')
for a in np.arange(len(p['lon'][0])):
    axes[2,2].scatter(p['lon'][0][a][0],p['lat'][0][a][0],color='green')
    if len(p['lon'][0][a])>=361:
        
        axes[2,2].scatter(p['lon'][0][a][360],p['lat'][0][a][360],color='red')
    #print len(lon[a])
        axes[2,2].plot([p['lon'][0][a][0],p['lon'][0][a][360]],[p['lat'][0][a][0],p['lat'][0][a][360]],'y-')#,linewidth=0.5)
    else:
        
        axes[2,2].scatter(p['lon'][0][a][-1],p['lat'][0][a][-1],color='red')
        axes[2,2].plot([p['lon'][0][a][0],p['lon'][0][a][-1]],[p['lat'][0][a][0],p['lat'][0][a][-1]],'y-')#,linewidth=0.5)
  
axes[2,2].scatter(p['lon'][0][a][0],p['lat'][0][a][0],label='start',color='green')
axes[2,2].scatter(p['lon'][0][a][-1],p['lat'][0][a][-1],label='end',color='red')  
axes[2,2].set_xlabel('2015')
axes[2,2].set_yticklabels([])
axes[2,2].set_xticklabels([])
axes[2,2].set_xlim([-69.5,-65])
axes[2,2].set_ylim([43.4,45.6]) 
"""
plt.savefig('FVCOM'+'_'+date,dpi=200)
plt.show()