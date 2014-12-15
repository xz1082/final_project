# -*- coding: utf-8 -*-
"""
Functions used to get the map with google static map api

Author:  Qingxian Lai (ql516)

"""
import pandas as pd
from cStringIO import StringIO
import urllib
try:
    from PIL import Image
except:
    import Image




def plot_the_location_map(df, num, keyword):
    """
    Draw a map to show all the job location on the list

    Argument
    ========
    df: Dataframe
    num: maximen number of point on the map
    keyword: the job list keyword

    """
    if len(df) < num:
        num = len(df)
    df = df[['Job ID', 'Business Title']]
    geo_map = pd.read_csv('NYC_Official_Jobs/id_geo_location.csv', index_col='Job ID')

    #===========marker======================================================
    marker_start = "markers=color:red"
    marker = marker_start
    for i in range(num):
        job_id = df.iloc[i, 0]
        lat = geo_map.loc[job_id, 'lat']
        lng = geo_map.loc[job_id, 'lng']
        marker = marker+"%7C{},{}".format(lat, lng)

    #==========parameters======================================================
    url_start = "http://maps.googleapis.com/maps/api/staticmap?"
    center_point = 'center=New+York+City'    
    size = "size=800x800"
    zoom = "zoom=11"
    sensor = "sensor=false"    
    maptype = "maptype=terrain"  # satellite ; terrain
    c = '&'
    url = url_start+center_point+c+size+c+zoom+c+marker+c+maptype+c+sensor

    #=======plot================================================================   
    buffered = StringIO(urllib.urlopen(url).read())
    image = Image.open(buffered)
    image.show()


def plot_one_job_location(job_id):
    """
    show the job location on the map

    Argument
    ========
    job_id:   the job's id

    """
    geo_map = pd.read_csv('NYC_Official_Jobs/id_geo_location.csv', index_col='Job ID')

    #===========marker======================================================
    marker_start = "markers=color:red"
    marker = marker_start

    lat = geo_map.loc[job_id, 'lat']
    lng = geo_map.loc[job_id, 'lng']
    marker = marker+"%7C{},{}".format(lat, lng)

    #==========parameters======================================================
    url_start = "http://maps.googleapis.com/maps/api/staticmap?"
    center_point = "center=%4.5f,%4.5f" % (lat, lng)
    size = "size=800x800"
    zoom = "zoom=14"
    sensor = "sensor=false"
    maptype = "maptype=terrain"
    c = '&'
    url = url_start+center_point+c+size+c+zoom+c+marker+c+maptype+c+sensor

    #=======plot================================================================
    buffered = StringIO(urllib.urlopen(url).read())
    image = Image.open(buffered)
    image.show()

