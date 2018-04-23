# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 14:55:33 2017

@author: huimin
from xiaojian CCB_fig10c
"""
import numpy as np
import matplotlib.pyplot as plt


fig=plt.figure(figsize=(9,12))
plt.subplots_adjust(wspace=0.1,hspace=0.1)
FNCL='necscoast_worldvec.dat'
CL=np.genfromtxt(FNCL,names=['lon','lat'])

####################################first######################################
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
lon1=[41.7251,41.7512,41.7011,41.6339,41.4167,41.5167,42.0157,42.0376,41.8959,41.4333]#1991
lat1=[-70.3625,-70.0455,-69.95,-70.3508,-70.9333,-70.7017,-70.1692,-70.0867,-70.0453,-70.9181]#1991
#lon1=[-70.3625,-70.0455,-70.4729,-70.1905,-69.9989,-70.1786,-70.4953,-70.0867,-70.6685,-70.0729,-70.2465]#year:2004        
#lat1=[41.7251,41.7512,41.3744,41.7411,41.7996,42.0584,41.7682,42.0376,41.7200,41.9259,41.6434]#year:2004
#lon1=[-70.3625,-70.5566,-70.0455,-70.1905,-69.9989,-70.6253,-70.2054,-69.9761,-70.1786,-70.4953,-70.0867,-70.6685,-70.0453,-70.2465]#year:2010
#lat1=[41.7251,41.7704,41.7512,41.7411,41.7996,41.5409,41.2733,41.7859,42.0584,41.7682,42.0376,41.7200,41.8959,41.6434]#year:2010

ax1.axis([-71.05,-69.8,41.25,42.35])
for a in np.arange(len(num1)):
    ax1.scatter(lon1[a],lat1[a],s=num1[a]*3,color='red')

ax1.plot(CL['lon'],CL['lat'])

ax1.text(lon1[0]-0.1,lat1[0]+0.02,towns1[0])
ax1.text(lon1[1],lat1[1],towns1[1])
ax1.text(lon1[2]-0.1,lat1[2]+0.04,towns1[2])
ax1.text(lon1[3],lat1[3],towns1[3])
ax1.text(lon1[4],lat1[4],towns1[4])
ax1.text(lon1[5],lat1[5],towns1[5])
ax1.text(lon1[6],lat1[6],towns1[6])
ax1.text(lon1[7],lat1[7]-0.03,towns1[7])
ax1.text(lon1[8]-0.1,lat1[8]+0.04,towns1[8])
ax1.text(lon1[9],lat1[9],towns1[9])
ax1.text(lon1[10],lat1[10],towns1[10])
ax1.text(lon1[11],lat1[11],towns1[11])
ax1.text(lon1[12],lat1[12],towns1[12])
ax1.text(lon1[13],lat1[13],towns1[13])


ax1.set_title('1991',fontsize=15)
#ax1.set_xlabel('lon')
#ax1.set_ylabel('lat',fontsize=15)
ax1.set_xticklabels([])
ax1.set_yticklabels([])
#for tick in ax1.yaxis.get_major_ticks():  
#    tick.label1.set_fontsize(13)
######################################second############################################
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
lon2=[41.7251,41.7512,41.7411,42.0083,41.7511,41.7996,41.8342,41.785,41.7506,41.9583,41.9172,41.4125]#1992
lat2=[-70.3625,-70.0455,-70.1905,-70.6717,-70.1506,-69.9989,-70.5342,-70.0172,-70.4508,-70.0783,-70.0678,-70.5456]#1992
#lon2=[-70.0455,-69.9955,-70.1925,-69.9989,-69.9761,-70.0867,-70.0453]#2005
#lat2=[41.7251,41.6673,41.7411,41.7996,41.7859,42.0376,41.8959]#2005
#lon2=[-70.3625,-70.5566,-70.0455,--70.1905,-69.9989,-70.6253,-70.6203,-69.9761,-70.1786,-70.4953,-70.0867,-70.0453,-70.9299,-70.5456]#year:2011
#lat2=[41.7251,41.7704,41.7512,41.7411,41.7996,41.5409,41.3925,41.7859,42.0584,41.7682,42.0376,41.8959,42.2393,41.4125]#year:2011
ax2.axis([-71.05,-69.8,41.25,42.35])
for a in np.arange(len(num2)):
    ax2.scatter(lon2[a],lat2[a],s=num2[a]*3,color='red')

ax2.plot(CL['lon'],CL['lat'])
"""
ax2.text(lon2[0],lat2[0],towns2[0])
ax2.text(lon2[1],lat2[1],towns2[1])
ax2.text(lon2[2]-0.1,lat2[2]-0.03,towns2[2])
ax2.text(lon2[3],lat2[3],towns2[3])
ax2.text(lon2[4],lat2[4],towns2[4])
ax2.text(lon2[5],lat2[5],towns2[5])
ax2.text(lon2[6],lat2[6],towns2[6])
ax2.text(lon2[7],lat2[7]-0.03,towns2[7])
ax2.text(lon2[8]-0.1,lat2[8]+0.03,towns2[8])
ax2.text(lon2[9],lat2[9],towns2[9])
ax2.text(lon2[10],lat2[10],towns2[10])
ax2.text(lon2[11],lat2[11],towns2[11])
ax2.text(lon2[12],lat2[12],towns2[12])
ax2.text(lon2[13],lat2[13],towns2[13])
"""
ax2.set_title('1992',fontsize=15)
ax2.set_yticklabels([])
ax2.set_xticklabels([])
#ax2.set_xlabel('lon')
#ax2.set_ylabel('lat')
##########################################third#############################################
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
lon3=[41.7251,41.7704,41.7512,41.6673,41.6130,41.7411,41.7426,41.7996,41.7859,42.0584,42.0376,41.8959,41.4125]#1999
lat3=[-70.3625,-70.5566,-70.0455,-69.9955,-70.9705,-70.1905,-70.1620,-69.9989,-69.9761,-70.1786,-70.0867,-70.0453,-70.5456]#1999
#lon3=[-70.8008,-70.3625,-70.5566,-70.0455,-70.1905,-69.9989,-69.9761,-70.1786,-70.4953,-70.0867,-70.0453]#2006
#lat3=[41.3352,41.7251,41.7704,41.7512,41.7411,41.7996,41.7859,42.0584,41.7682,42.0376,41.8959]#2006
#lon3=[-70.3625,-70.5566,-70.0455,-70.1905,-70.1620,-69.9989,-70.6253,-70.8898,-70.8535,-70.2054,-69.9761,-70.1786,-70.4953,-70.0867,-70.6685,-70.0453,-70.6731,-70.2465,-70.2588,-70.5456]#2012
#lat3=[41.7251,41.7704,41.7512,41.7411,41.7426,41.7996,41.5409,42.2418,42.2693,41.2733,41.7859,41.8109,41.7682,42.0376,41.72,41.8959,41.5265,41.6434,41.7081,41.4125]#2012

ax3.axis([-71.05,-69.8,41.25,42.35])
for a in np.arange(len(num3)):
    ax3.scatter(lon3[a],lat3[a],s=num3[a]*3,color='red')
ax3.plot(CL['lon'],CL['lat'])
"""
ax3.text(lon3[0]-0.1,lat3[0],towns3[0])
ax3.text(lon3[1]-0.08,lat3[1],towns3[1])
ax3.text(lon3[2],lat3[2]-0.05,towns3[2])
ax3.text(lon3[3]-0.08,lat3[3]+0.03,towns3[3])
ax3.text(lon3[4],lat3[4],towns3[4])
ax3.text(lon3[5],lat3[5],towns3[5])
ax3.text(lon3[6],lat3[6],towns3[6])
ax3.text(lon3[7]-0.02,lat3[7]-0.03,towns3[7])
ax3.text(lon3[8],lat3[8],towns3[8])
ax3.text(lon3[9],lat3[9],towns3[9])
ax3.text(lon3[10],lat3[10]-0.03,towns3[10])
ax3.text(lon3[11],lat3[11],towns3[11])
ax3.text(lon3[12],lat3[12],towns3[12])
ax3.text(lon3[13],lat3[13],towns3[13])
ax3.text(lon3[14],lat3[14],towns3[14])
ax3.text(lon3[15],lat3[15],towns3[15])
ax3.text(lon3[16]-0.1,lat3[16]-0.04,towns3[16])
ax3.text(lon3[17],lat3[17]-0.04,towns3[17])
ax3.text(lon3[18],lat3[18]-0.04,towns3[18])
"""
ax3.set_title('1999',fontsize=15)
#ax3.set_xlabel('lon')
#ax3.set_ylabel('lat',fontsize=15)
ax3.set_xticklabels([])
ax3.set_yticklabels([])
for tick in ax3.yaxis.get_major_ticks():  
    tick.label1.set_fontsize(13)
############################################fourth#############################################
ax4=fig.add_subplot(3,2,4)
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
lon4=[41.7251,41.7512,41.7411,41.7996,41.7859,42.0376,41.8959,41.7081]#2001
lat4=[-70.3625,-70.0455,-70.1905,-69.9989,-69.9761,-70.0867,-70.0453,-70.2588]#2001
#lon4=[-70.0455,-70.1905,-69.9989,-70.0329,-70.0168,-70.0867,-70.0729]#2007
#lat4=[41.7512,41.7411,41.7996,41.3165,41.7949,42.0376,41.9259]#2007
#lon4=[-70.3625,-70.0455,-70.0714,-70.1905,-69.9989,-69.9761,-70.1786,-70.0867,-70.0453,-70.0763]#2013
#lat4=[41.7251,41.7512,41.9417,41.7411,41.7996,41.7859,42.0584,42.0376,41.8959,41.9428]#2013

ax4.axis([-71.05,-69.8,41.25,42.35])
for a in np.arange(len(num4)):
    ax4.scatter(lon4[a],lat4[a],s=num4[a]*3,color='red')
ax4.plot(CL['lon'],CL['lat'])
"""
ax4.text(lon4[0],lat4[0],towns4[0])
ax4.text(lon4[1]-0.05,lat4[1]-0.05,towns4[1])
ax4.text(lon4[2],lat4[2],towns4[2])
ax4.text(lon4[3],lat4[3],towns4[3])
ax4.text(lon4[4],lat4[4],towns4[4])
ax4.text(lon4[5],lat4[5]-0.03,towns4[5])
ax4.text(lon4[6]-0.1,lat4[6]-0.04,towns4[6])
ax4.text(lon4[7],lat4[7],towns4[7])
ax4.text(lon4[8],lat4[8],towns4[8])
"""
ax4.set_title('2001',fontsize=15)
ax4.set_yticklabels([])
ax4.set_xticklabels([])
#ax4.set_xlabel('lon')
#ax4.set_ylabel('lat')
################################fifth#######################################3
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
lon5=[41.7251,41.7512,41.7411,41.7996,41.7859,42.0584,42.0376,41.8959,41.7081,41.4125]#2002
lat5=[-70.3625,-70.0455,-70.1905,-69.9989,-69.9761,-70.1786,-70.0867,-70.0453,-70.2588,-70.5456]#2002
#lon5=[-70.3625,-70.0455,-70.1905,-69.9989,-70.6203,-69.9761,-70.1786,-70.0867,-70.0453]#2008
#lat5=[41.7251,41.7512,41.7411,41.7996,41.3925,41.7859,42.0584,42.0376,41.8959]#2008
#lon5=[-70.3625,-70.5566,-70.0455,-69.9955,-70.1905,-69.9989,-70.6253,-70.9,-70.6203,-70.2054,-70.0953,-69.9761,-70.1786,-70.4953,-70.0867,-70.0453,-70.6345,-70.2588,-71.8384]#2014
#lat5=[41.7251,41.7704,41.7512,41.6673,41.7411,41.7996,41.5409,42.3062,41.3925,41.2733,42.0334,41.7859,42.0584,41.7682,41.9948,41.8959,41.6042,41.7081,42.2599]#2014
ax5.axis([-71.05,-69.8,41.25,42.35])
for a in np.arange(len(num5)):
    ax5.scatter(lon5[a],lat5[a],s=num5[a]*3,color='red')

ax5.plot(CL['lon'],CL['lat'])

"""
ax5.text(lon5[0],lat5[0],towns5[0])
ax5.text(lon5[1]-0.1,lat5[1],towns5[1])
ax5.text(lon5[2]-0.1,lat5[2],towns5[2])
ax5.text(lon5[3],lat5[3],towns5[3])
ax5.text(lon5[4],lat5[4],towns5[4])
ax5.text(lon5[5],lat5[5],towns5[5])
ax5.text(lon5[6],lat5[6],towns5[6])
ax5.text(lon5[7],lat5[7],towns5[7])
ax5.text(lon5[8],lat5[8],towns5[8])
ax5.text(lon5[9],lat5[9],towns5[9])
ax5.text(lon5[10],lat5[10],towns5[10])
ax5.text(lon5[11],lat5[11]-0.03,towns5[11])
ax5.text(lon5[12]-0.1,lat5[12]+0.04,towns5[12])
ax5.text(lon5[13],lat5[13],towns5[13])
ax5.text(lon5[14],lat5[14],towns5[14])
ax5.text(lon5[15],lat5[15],towns5[15])
ax5.text(lon5[16],lat5[16],towns5[16])
ax5.text(lon5[17],lat5[17]-0.05,towns5[17])
ax5.text(lon5[18],lat5[18],towns5[18])
"""
ax5.set_title('2002',fontsize=15)

#ax5.set_xlabel('lon',fontsize=15)
#ax5.set_ylabel('lat',fontsize=15)
ax5.set_yticklabels([])
ax5.set_xticklabels([])
#for tick in ax5.xaxis.get_major_ticks():  
#    tick.label1.set_fontsize(13)
#for tick in ax5.yaxis.get_major_ticks():  
#    tick.label1.set_fontsize(13)
#############################sixth#################################################
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
lon6=[41.7251,41.7512,41.7411,41.7996,41.7859,41.8109,42.0584,41.7682,42.0376,41.8959,41.7081]#2003
lat6=[-70.3625,-70.0455,-70.1905,-69.9989,-69.9761,-70.5451,-70.1786,-70.4953,-70.0867,-70.0453,-70.2588]#2003
#lon6=[-70.3625,-70.5566,-70.0455,-70.1905,-69.9989,-70.6253,-70.9,-69.9761,-71.0023,-70.4953,-70.0867,-70.0453,-70.6569,-70.6203,-70.5456]#2009
#lat6=[41,7251,41.7704,41.7512,41.7411,41.7996,41.5409,42.3062,41.7859,42.2529,41.7682,42.0376,41.8959,41.3473,41.3925,41.4125]#2009
#lon6=[-70.3625,-70.0455,-70.1905,-70.6723,-69.9989,-70.6253,-70.8898,-70.9,-70.0203,-69.9761,-70.5451,-70.1786,-70.4953,-70.0867,-70.6656,-70.0453,-70.6673,-70.2465,-70.1127]#2015
#lat6=[41.7251,41.7512,41.7411,42.0418,41.7996,41.5409,42.2418,42.3062,41.3043,41.7859,41.8109,42.0584,41.7682,42.0376,41.7249,41.8959,41.4382,41.6434,41.7776]#2015

ax6.axis([-71.05,-69.8,41.25,42.35])
for a in np.arange(len(num6)):
    ax6.scatter(lon6[a],lat6[a],s=num6[a]*3,color='red')
ax6.plot(CL['lon'],CL['lat'])
"""
ax6.text(lon6[0],lat6[0],towns6[0])
ax6.text(lon6[1]-0.05,lat6[1]-0.03,towns6[1])
ax6.text(lon6[2],lat6[2],towns6[2])
ax6.text(lon6[3],lat6[3],towns6[3])
ax6.text(lon6[4],lat6[4]-+0.03,towns6[4])
ax6.text(lon6[5],lat6[5],towns6[5])
ax6.text(lon6[6],lat6[6]-0.02,towns6[6])
ax6.text(lon6[7],lat6[7],towns6[7])
ax6.text(lon6[8],lat6[8],towns6[8])
ax6.text(lon6[9],lat6[9],towns6[9])
ax6.text(lon6[10]-0.03,lat6[10],towns6[10])
ax6.text(lon6[11]-0.06,lat6[11]+0.03,towns6[11])
ax6.text(lon6[12],lat6[12],towns6[12])
ax6.text(lon6[13],lat6[13],towns6[13])
ax6.text(lon6[14],lat6[14],towns6[14])
ax6.text(lon6[15],lat6[15],towns6[15])
ax6.text(lon6[16],lat6[16],towns6[16])
ax6.text(lon6[17],lat6[17],towns6[17])
ax6.text(lon6[18],lat6[18],towns6[18])
"""
ax6.set_title('2003',fontsize=15)
ax6.set_yticklabels([])
ax6.set_xticklabels([])
#for tick in ax6.xaxis.get_major_ticks():  
#    tick.label1.set_fontsize(13)
#ax6.set_xlabel('lon',fontsize=15)
#ax6.set_ylabel('lat')
plt.suptitle('strandings_by_town',fontsize=18)
plt.savefig('strandings_1991-2003_town',dpi=100,bbox_inches="tight")
plt.savefig('strandings_1991-2003_town'+'.ps',dpi=100,bbox_inches="tight")
