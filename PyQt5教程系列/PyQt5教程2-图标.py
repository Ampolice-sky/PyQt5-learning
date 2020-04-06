#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyQt5教程2：
在这个例子中，我们创建了一个图标。
作者:Jane Bodnar
网站:py40.com
最后编辑:2015年1月
改写:Ampolice-sky Kevin
修改时间：2020.4.6
"""

from sys import *
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from os import *
environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'E:\我的Python项目\Pygame\五子棋\venv\Lib\site-packages\PyQt5\Qt\plugins'


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        # 设置窗口的位置和大小，前两个是位置，后两个是大小（x, y, weight, height)
        self.setGeometry(300, 300, 300, 220)
        # 设置窗口的标题
        self.setWindowTitle('标题')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('web.png'))

        # 显示窗口
        self.show()


# 创建应用程序和对象
app = QApplication(argv)
ex = Example()
exit(app.exec_())
