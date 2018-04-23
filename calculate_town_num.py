# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 09:27:48 2017

@author: huimin
calculate the number of each town per year
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

c1 = np.genfromtxt('strandings_2012_only_town.csv',dtype=None,names=['turtle_ID','date','town'],delimiter=',',skip_header=1)
c1['town']=np.char.capitalize(c1['town'])
#for item in c1['town']:
 #   print c1['town'].count(item),"of",item
print pd.value_counts(c1['town'])
"""
towns1=[]
count=0
for a in c1['town']:
    #print a
    if a not in towns1:
        towns1.append(a)
print towns1
num1=[]
for a in np.arange(len(towns1)):
    j=0
    for b in np.arange(len(c1['town'])):
        if towns1[a]==c1['town'][b]:
            j=j+1
    num1.append(j)
"""