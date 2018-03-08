# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 15:50:45 2017

@author: xiaojian
modified by huimin in Feb 2018
"""


import datetime as dt
from datetime import timedelta
import numpy as np
from barycentric_polygonal_interpolation import get_fvcom
######## Hard codes ##########
Model='30yr'
wind_get_type='FVCOM'
wind=0 
st_lat=[]
st_lon=[]
latc=np.linspace(41.8,42.0,10)
lonc=np.linspace(-70.5,-70.2,10)
for aa in np.arange(len(lonc)):
    for bb in np.arange(len(latc)):
        st_lat.append(latc[bb])
        st_lon.append(lonc[aa])
'''
num = 70
st_lat = np.random.uniform(44.5,45,num)[:]
st_lon = np.random.uniform(-66.8,-66,num)[:]
'''
days=7                                                                                                                                                         

end_times=[]
start_time=[dt.datetime(2014,11,18,0,0,0,0)]
#start_times=[dt.datetime(2015,5,1,0,0,0,0),dt.datetime(2014,5,1,0,0,0,0)]#,dt.datetime(2013,5,1,0,0,0,0),dt.datetime(2012,5,1,0,0,0,0),dt.datetime(2011,5,1,0,0,0,0),dt.datetime(2010,5,1,0,0,0,0),dt.datetime(2009,5,1,0,0,0,0),dt.datetime(2008,5,1,0,0,0,0),dt.datetime(2007,5,1,0,0,0,0)]
#for a in np.arange(len(start_times)):
    #start_time.append(start_times[a]+timedelta(hours=jia*24))
m_ps =dict(lon=[],lat=[],time=[],num_ashore=[])
for a in np.arange(len(start_time)):
    #print a
    end_time=start_time[a]+timedelta(hours=days*24)
    
    GRIDS= ['GOM3','massbay','30yr']
    if Model in GRIDS:
        try:
            get_obj =  get_fvcom(Model)
            #url_fvcom = get_obj.get_url(start_time[a],end_time)            
            #b_points = get_obj.get_data(url_fvcom)

            model_points =dict(lon=[],lat=[],time=[],num_ashore=[])
            for b in np.arange(len(st_lon)):
                
                modelpoints = dict(lon=[],lat=[],time=[],num_ashore=[])
                modelpoints,windspeed= get_obj.get_track(st_lon[b],st_lat[b],0,start_time[a],wind,wind_get_type)
                
                model_points['lon'].append(modelpoints['lon'])
                model_points['lat'].append(modelpoints['lat'])
                model_points['time'].append(modelpoints['time'])
                model_points['num_ashore'].append(modelpoints['num_ashore'])
        except:
            print 'There is no model-point near the given-point'
            continue
    m_ps['lon'].append(model_points['lon'])
    m_ps['lat'].append(model_points['lat'])
    m_ps['time'].append(model_points['time'])
    m_ps['num_ashore'].append(model_points['num_ashore'])
    
np.save(Model+'_'+wind_get_type+str(start_time[0].year)+str(start_time[0].month)+str(start_time[0].day)+'_'+str(days)+'days',m_ps)