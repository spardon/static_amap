# coding: utf-8
import requests
from io import BytesIO
from PIL import Image


def get_image(center):
    url = "http://restapi.amap.com/v3/staticmap?location={}"\
           "&zoom=14&size=1024*1024&key=868c7ad6dc9c8ceb424b6b747d4ee336&scale=2".format(center)
    box = (1024, 1024, 2048, 2048)
    ori_image = Image.open(BytesIO(requests.get(url).content))
    crop_img = ori_image.crop(box)
    return crop_img


def merge_img_test(a, b):
    base_image = Image.new('RGB', (2048, 1024))
    base_image.paste(a, (0, 0))
    base_image.paste(b, (1024, 0))
    base_image.save('./test.png')


if __name__ == '__main__':
    # dd = 0.022156241379310528 - 0.00022
    dd = 0.02270199999999889 - 0.00075
    lng = 26.566408
    lat = 106.689546
    aa = get_image('{},{}'.format(lat, lng))
    bb = get_image('{},{}'.format(lat+dd, lng))
    merge_img_test(aa, bb)
