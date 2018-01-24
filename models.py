# -*- coding: utf-8 -*-
from utils import distance


class AmapPic(object):
    """
    获取到的静态地图相关参数
    """
    def __init__(self, center, width, height, number=0):
        self.center = center
        self.width = width
        self.height = height
        self.number = number


class CityInfo(object):
    def __init__(self, lat1, lng1, lat2, lng2):
        self.city_lat1 = lat1
        self.city_lng1 = lng1

        self.city_lat2 = lat2
        self.city_lng2 = lng2

        # 图片对应实际距离宽度的一半
        self.zone_l = 2020

        self.city_l = distance(lat1, lng1, lat1, lng2)
        self.city_w = distance(lat1, lng1, lat2, lng1)

        self.zone_lc = int(self.city_l / self.zone_l)
        self.zone_wc = int(self.city_w / self.zone_l)

        self.acc_l = (lng2 - lng1) / self.zone_lc
        self.acc_w = (lat2 - lat1) / self.zone_wc