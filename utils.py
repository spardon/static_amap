# -*- coding: utf-8 -*-
import math
import requests
from config import AMAP_KEY, STATIC_MAP_URL


def distance(lat1, lng1, lat2, lng2):
    """
    计算两个经纬度坐标点的距离
    :param lat1: o 点 纬度
    :param lng1: o 点 经度
    :param lat2: d 点 纬度
    :param lng2: d 点 经度
    :return: od 距离
    """
    lat1 = float(lat1)
    lng1 = float(lng1)
    lat2 = float(lat2)
    lng2 = float(lng2)
    pi = math.pi
    earth_r = 6378137
    rad = pi / 180.0
    rad_lat1 = lat1 * rad
    rad_lat2 = lat2 * rad

    a = rad_lat1 - rad_lat2
    b = (lng1 - lng2) * rad
    s = 2 * math.asin(math.sqrt(math.pow(math.sin(a / 2), 2)
                                + math.cos(rad_lat1) * math.cos(rad_lat2)
                                * math.pow(math.sin(b / 2), 2)
                                )
                      )
    s = s * earth_r
    return s


def get_static_map(center):
    """
    根据地图中心点获取
    :param center:
    :return:
    """
    # "location=106.689546,26.566408&zoom=17&size=1024*1024&key=868c7ad6dc9c8ceb424b6b747d4ee336&scale=2"
    param = {
        'location': '{},{}'.format(center[0], center[1]),
        'zoom': 17,
        'size': '1024*1024',
        'key': AMAP_KEY,
        'scale': 2,
    }

    rep = requests.get(url=STATIC_MAP_URL, params=param)

    return rep.content



