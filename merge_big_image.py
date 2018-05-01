# -*- coding: utf-8 -*-
import os
import re
from PIL import Image


def confirm_image_size(img_path):
    """
    确定图片大小和数量
    :param path:
    :return:
    """
    img_list = os.listdir(img_path)
    max_row = max([int(re.findall('(\d+)_\d+\.png', img)[0]) for img in img_list]) + 1
    max_col = max([int(re.findall('\d+_(\d+)\.png', img)[0]) for img in img_list]) + 1
    h_num = max_row // 10
    last_h_num = max_row % 10
    img_sizes = [(max_col, h*10) for h in range(1, h_num + 1)]
    img_sizes.append((max_col, max_row))
    return img_sizes


def merge(img_sizes, img_path, r_path):
    # img_sizes = [(44, 45)]
    print(img_sizes)
    sim_height = 915
    box = (960, 0, 1920, sim_height)
    for w, h in img_sizes:
        im_h = 10 if h % 10 == 0 else (h % 10) + 1
        im = Image.new('RGB', (960*w, sim_height*im_h), (0, 0, 0))
        for i in range(h-im_h, h):
            for j in range(0, w):
                print(i, j)
                sim = Image.open(os.path.join(img_path, '{}_{}.png'.format(i, j)), 'r')
                c_im = sim.crop(box)
                im.paste(c_im, (960*j, sim_height*(i % 10)))
                print(960*j, sim_height*(i % 10))

        im.save(os.path.join(r_path, '{}_{}.png'.format(w, h)))
        im.close()


if __name__ == '__main__':
    img_sizes = confirm_image_size('./img')
    merge(img_sizes, './img', './res_img')

