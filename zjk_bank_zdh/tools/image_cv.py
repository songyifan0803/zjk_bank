#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import cv2, time
from PIL import ImageGrab
from pykeyboard import PyKeyboard
from pymouse import PyMouse
from AC_frame.tools.common import Common

class ImageMatch:
    logger = Common.write_log()
    mouse = PyMouse()
    @classmethod
    def find_image(cls,target):
        """
        通过Opencv进行图片识别，识别成功则返回中心坐标
        :param target:模板图片名称
        :param similarity:0-1之间的小数，自定义模板图片与对比图的相似度。
        :return: 坐标元组
        """
        image_path = os.path.join(os.getcwd(),'image')
        screen_path = os.path.join(image_path,'screen_shop.png')
        ImageGrab.grab().save(screen_path)
        screen = cv2.imread(screen_path)
        template = cv2.imread(os.path.join(image_path,target))
        result = cv2.matchTemplate(screen,template,cv2.TM_CCOEFF_NORMED)
        min, max, min_loc, max_loc = cv2.minMaxLoc(result)
        similarity = Common.get_ini("../config/config_data.ini", 'imagematch', 'similarity')
        if max < similarity:
            return -1,-1
        x = max_loc[0]+int(template.shape[1]/2)
        y = max_loc[1]+int(template.shape[0]/2)
        return x,y

    @classmethod
    def image_click(cls, target, sleep_time=0.5):
        """
        单击图片识别找到的元素的坐标
        :param target: 图片名称
        :param sleep_time: 点击后的睡眠时间
        :return:None
        """
        mouse = PyMouse()
        x,y = ImageMatch.find_image(target)
        try:
            mouse.click(x, y)
            cls.logger.info("在位置[%d:%d]进行单击操作." % (x, y))
        except:
            cls.logger.error("在位置[%d,%d]进行单击操作失败." % (x, y))
        time.sleep(sleep_time)

    @classmethod
    def image_double_click(cls,target, sleep_time=0.5):
        """
        双击图片识别找到的元素的坐标
        :param target: 图片名称
        :param sleep_time: 点击后的睡眠时间
        :return:None
        """
        x,y = ImageMatch.find_image(target)
        try:
            cls.mouse.click(x=x, y=y, button=1, n=2)
            cls.logger.info("在位置[%d,%d]进行双击操作." % (x, y))
        except:
            cls.logger.error("在位置[%d,%d]进行双击操作失败." % (x, y))
        finally:
            time.sleep(sleep_time)

    @classmethod
    def image_right_click(cls,target, sleep_time=0.5):
        """
        右键单击图片识别找到的元素的坐标
        :param target: 图片名称
        :param sleep_time: 点击后的睡眠时间
        :return:None
        """
        x,y = ImageMatch.find_image(target)
        try:
            cls.mouse.click(x=x, y=y, button=2, n=1)
            cls.logger.info("在位置[%d,%d]进行双击操作." % (x, y))
        except:
            cls.logger.error("在位置[%d,%d]进行双击操作失败." % (x, y))
        finally:
            time.sleep(sleep_time)

    @classmethod
    def random_input(cls,target, str ,sleep_time=0.5):
        """
        在图片识别元素处输入
        :param target: 模板图片名
        :param str: 要输入的字符串
        :param sleep_time: 睡眠时间
        :return:
        """
        x, y = ImageMatch.find_image(target)
        PyKeyboard().type_string(str)
        try:
            cls.logger.info("在位置[%d,%d]进行输入操作" % (x, y))
        except:
            cls.logger.error("在位置[%d,%d]进行输入操作失败." % (x, y))
        finally:
            time.sleep(sleep_time)

if __name__ == '__main__':
    test = ImageMatch()
    test.image_double_click('ff.png')

