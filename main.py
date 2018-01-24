# -*- coding: utf-8 -*-
from PIL import Image
from io import BytesIO
from config import City
from models import CityInfo
import requests


def creat_image(img_l, img_h):
    """
    创建新的底图
    :param l: 底图长
    :param w: 底图宽
    :return:
    """
    return Image.new('RGB', (img_l, img_h), (0, 0, 0))


def get_crop_map(center):
    """
    设置地图中心点以及获取底图
    :return:
    """
    url = "http://restapi.amap.com/v3/staticmap?location={}" \
          "&zoom=14&size=1024*1024&key=868c7ad6dc9c8ceb424b6b747d4ee336&scale=2".format(center)
    box = (1024, 1024, 2048, 2048)
    print(url)
    ori_image = Image.open(BytesIO(requests.get(url).content))
    crop_img = ori_image.crop(box)
    return crop_img


if __name__ == '__main__':
    city = CityInfo(City.lat1, City.lng1, City.lat2, City.lng2)
    print(city.acc_l, city.acc_w)
    for w in range(city.zone_wc):
        # image = creat_image(city.zone_lc*1024, 1024)
        image = creat_image(10*1024, 1024)
        for l in range(city.zone_lc):
            print(l, w)
            cen = '{},{}'.format(city.city_lng1 + l*(city.acc_l+0.00122), city.city_lat1 + w*city.acc_w)
            cp_img = get_crop_map(cen)
            if l == 10:
                break
            image.paste(cp_img, (l*1024, w*1024))

        image.save('img/{}.png'.format(w))
        if w == 1:
            break

