#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 17:27:11 2019

@author: ayushitandon
"""

def clean_data(df):
    WeatherCode = ['FC', 'TS', 'GR', 'RA', 'DZ', 'SN', 'SG', 'GS', 'PL', 'IC', 'FG', 'BR', 'UP', 'HZ', 'FU', 'VA', 
               'DU', 'DS', 'PO', 'SA', 'SS', 'PY', 'SQ', 'DR', 'SH', 'FZ', 'MI', 'PR', 'BC', 'BL', 'VC', '+']
    df['Weather'] = pd.Series(list(map(lambda x: sum(list(map(lambda y: x.find(y) >= 0, WeatherCode))), df.codesum)), index = df.index)
    df = df.replace(('-', ' '), np.nan)
    df = df.replace('M', np.nan)
    df = df.replace(('T', '  T'), 0.001)
    num_attr = ['tmax', 'tmin', 'tavg', 'dewpoint', 'wetbulb', 'heat', 'cool', 'snowfall', 
                'preciptotal', 'stnpressure','sealevel', 'resultspeed', 'resultdir', 'avgspeed', 'units']
    df[num_attr] = df[num_attr].astype(float)
    df = df.loc[:,df.isnull().sum()< df.shape[0]*.5]
    return df

df1 = clean_data(df)
