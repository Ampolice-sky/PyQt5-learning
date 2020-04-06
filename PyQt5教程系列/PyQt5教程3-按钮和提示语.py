#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyQt5教程3：
在这个例子中，我们创建了一个简单的按钮，光标停留在上面时会出现提示语
作者:Jane Bodnar
网站:py40.com
最后编辑:2015年1月
改写:Ampolice-sky Kevin
修改时间：2020.4.6
"""

from sys import *
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont
from os import *
environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'E:\我的Python项目\Pygame\五子棋\venv\Lib\site-packages\PyQt5\Qt\plugins'
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 这种静态的方法设置一个用于显示工具提示的字体。我们使用10px滑体字体。
        QToolTip.setFont(QFont('SansSerif', 10))

        # 创建一个提示，我们称之为settooltip()方法。我们可以使用丰富的文本格式
        self.setToolTip('正常字体<b>强调字体</b>正常字体') # 实际上，在光标停留时，这里不会执行

        # 创建一个PushButton并为他设置一个tooltip
        btn = QPushButton('按钮', self)  # 此处的首项是按钮的名字
        btn.setToolTip('正常字体<b>强调字体</b>正常字体')

        # btn.sizeHint()显示默认尺寸
        btn.resize(btn.sizeHint())

        # 移动窗口的位置
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('标题') # 这里是标题
        self.show()

app = QApplication(argv)
ex = Example()
exit(app.exec_())

