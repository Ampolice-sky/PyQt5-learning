# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyQt5教程1：
在这个例子中，我们创建了一个简单的PyQt5中的窗口。 
作者:Jane Bodnar
网站:py40.com 
最后编辑:2015年1月
改写:Ampolice-sky Kevin
修改时间：2020.4.6
"""
# 这里我们提供必要的引用。基本控件位于PyQt5.Qtwidgets模块中。
# 若非大型项目，可以直接导入模块，此处使用全部导入目的是让编写方式变得更直白，更易理解。
from sys import *
from PyQt5.QtWidgets import QApplication, QWidget
from os import *

# 此处提供解释路径，按照电脑上plugins文件的位置填写，需引入Python自带的os模块。
environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'E:\我的Python项目\Pygame\五子棋\venv\Lib\site-packages\PyQt5\Qt\plugins'
# 每一PyQt5应用程序必须创建一个应用程序对象。argv参数是一个列表，从命令行输入参数。
app = QApplication(argv)
# QWidget部件是PyQt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。
w = QWidget()
# resize()方法调整窗口的大小。这离是350px宽250px高
w.resize(350, 250)
# move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
w.move(300, 300)
# 设置窗口的标题
w.setWindowTitle('我的第一个PyQt5项目')
# 显示在屏幕上
w.show()
# 系统exit()方法确保应用程序干净的退出
# QApplication的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替执行
exit(app.exec_())
# 代码到此为止，可以仔细研究一下代码，准备下一阶段的内容
