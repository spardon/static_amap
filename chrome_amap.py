# coding: utf-8
"""
利用 selenuim 进行截图
"""
import os
import time
from PIL import Image
from selenium import webdriver


def main(arr):
    to_origin = chrome.find_element_by_id("origin")
    level_move_ele = chrome.find_element_by_id("level")
    vertical_move_ele = chrome.find_element_by_id("vertical")
    for _, item in enumerate(arr):
        # if item[1] == 4 and item[0] == 2:
        #     break
        if item[1] == 0:
            # 重置会原点并进行位移，js 中记录点击次数
            to_origin.click()
            vertical_move_ele.click()
        else:
            # 水平位移
            level_move_ele.click()
        time.sleep(3)
        chrome.save_screenshot('{}_{}.png'.format(item[0], item[1]))


def meger_image(arr):
    # im = Image.new('RGB', (w*1280, h*686), (0, 0, 0))
    im = Image.new('RGB', (29*1280, 33*686), (0, 0, 0))
    for item in arr:
        if item[0] == 29:
            break
        cur_im = Image.open('{}_{}.png'.format(item[0], item[1]))
        box = (1280, 686, 2560, 1372)
        c_im = cur_im.crop(box)

        im.paste(c_im, (item[1]*1280, item[0]*686))
    im.save('res.png')


if __name__ == '__main__':
    # chrome = webdriver.Chrome('./chromedriver')
    # fp = os.path.join(os.getcwd(), 'amap.html')
    # chrome.get('file://{}'.format(fp))
    # chrome.maximize_window()
    acc_w = 0.05484400000000278
    acc_h = 0.0268519999999981

    top_y = 26.806842
    left_x = 106.293911
    right_x = 106.868245
    bottom_y = 26.48024

    w = int(((right_x - left_x) // acc_w) + 1) * 3
    h = int(((top_y - bottom_y) // acc_h) + 1) * 3
    print(w, h)
    zone_arr = []

    for i in range(h):
        for j in range(w):
            zone_arr.append([i, j])
    time.sleep(5)

    # main(zone_arr)

    meger_image(zone_arr)
    # chrome.close()

