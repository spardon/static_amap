#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import time
from selenium import webdriver
from PIL import Image


def get_split_img(browser, ori, le, ver):
    """
    获取多个分割的图片
    """
    level_num = 0
    vertical_num = 0
    first = 1
    while 1:
        flag = int(browser.find_element_by_id('start').get_attribute('value'))
        if flag == 0:
            continue
        elif flag == 2:
            break
        else:
            if first:
                first -= 1
                time.sleep(1)
            if int(browser.find_element_by_id('level_num').get_attribute('value')) == 0:
                # print(vertical_num, level_num)
                browser.save_screenshot('./img/{}_{}.png'.format(vertical_num, level_num))
                le.click()
                level_num += 1
            else:
                # 先对上次末尾进行截图
                # print(vertical_num, level_num)
                level_num = 0
                vertical_num += 1
                ori.click()
                time.sleep(1)
                ver.click()
                # browser.save_screenshot('./img/{}_{}.png'.format(vertical_num, level_num))
        time.sleep(3)


def merge_image(path):
    """
    将多个地图图片合并
    :return:
    """
    imgs = os.listdir(path)
    im_height = 915
    w = len([w_i for w_i in imgs if w_i.startswith('0_')])
    h = len([h_i for h_i in imgs if h_i.endswith('_0.png')])
    im = Image.new('RGB', (w * 960, int(h * im_height)), (0, 0, 0))
    box = (960, 0, 1920, im_height)
    img_li = [[int(i) for i in o.split('.')[0].split('_')] for o in imgs]

    img_li.sort(key=lambda s: (s[0], s[1]))
    for item in img_li:
        cur_im = Image.open('./img/{}_{}.png'.format(item[0], item[1]))
        box = (960, 0, 1920, im_height)
        c_im = cur_im.crop(box)
        im.paste(c_im, (item[1] * 960, item[0] * im_height))

    im.save('res.png')


def main(filename):
    img_path = os.path.join(os.getcwd(), 'img')
    if os.path.exists(img_path):
        img_dir = os.listdir(img_path)
        if len(img_dir):
            for img in img_dir:
                img = os.path.join(img_path, img)
                os.remove(img)
    else:
        os.mkdir(img_path)
    try:
        chrome = webdriver.Chrome('./chromedriver.exe')
        html_path = os.path.join(os.getcwd(), filename)
        chrome.get('file://{}'.format(html_path))
        # 在 mac 最大化窗口失败
        chrome.maximize_window()
        origin = chrome.find_element_by_id('origin')
        level = chrome.find_element_by_id('level')
        vertical = chrome.find_element_by_id('vertical')

        get_split_img(chrome, origin, level, vertical)

        # merge_image(img_path)

        # chrome.close()

        img_dir = os.listdir(img_path)
        # img_dir = []
        if len(img_dir):
            for img in img_dir:
                img = os.path.join(img_path, img)
                os.remove(img)
    except Exception as e:
        print(e)
    finally:
        chrome.close()

if __name__ == '__main__':
    argv = sys.argv
    if len(argv) != 2 or argv[-1] not in ['qq', 'amap', 'baidu']:
        exit(
            """
            Usage: python x.py qq/amap/baidu
            """        
        )

    map_map = {
        'qq': 'qq_static.html',
        'amap': 'amap_static.html',
        'baidu': 'baidu_static.html'
    }

    main(map_map[argv[-1]])
