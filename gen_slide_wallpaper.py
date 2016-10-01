#!/usr/bin/python3
# coding: utf-8
# This script provide simple tool to generate xml file for gnome|mate-appearance
# Just run script with one arg which is a dirname
# Every month new wallpaper here:
#   http://www.smashingmagazine.com/tag/wallpapers/

import sys
from os import listdir, path, getcwd
from lxml.etree import Element, SubElement, tostring

i_dir = sys.argv[1]
imgs = listdir(i_dir)
time = '300.0'
trans = '5.0'
dest = path.join('/usr/share/backgrounds', i_dir)

root = Element('background')
starttime = SubElement(root, 'starttime')
year = SubElement(starttime, 'year')
year.text = '2016'
month = SubElement(starttime, 'month')
month.text = '10'
day = SubElement(starttime, 'day')
day.text = '01'
hour = SubElement(starttime, 'hour')
hour.text = '00'
minute = SubElement(starttime, 'minute')
minute.text = '00'
second = SubElement(starttime, 'second')
second.text = '00'

for img in imgs:
    static = SubElement(root, 'static')
    duration = SubElement(static, 'duration')
    duration.text = time
    file = SubElement(static, 'file')
    file.text = path.join(dest, img)
    transition = SubElement(root, 'transition')
    duration_t = SubElement(transition, 'duration')
    duration_t.text = trans
    from_ = SubElement(transition, 'from')
    from_.text = file.text
    to = SubElement(transition, 'to')
    if img == imgs[-1]:
        to.text = path.join(dest, imgs[0])
    else:
        to.text = path.join(dest, imgs[imgs.index(img) + 1])
with open(path.join(getcwd(), i_dir + '/' + i_dir + '.xml'), 'w') as f:
    f.write(tostring(root, pretty_print=True, encoding='unicode'))
