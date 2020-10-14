from PyQt5.QtWidgets import *

def tab1UI(GWidget):
    # 表单布局
    layout = QFormLayout()
    # 添加姓名，地址的单行文本输入框
    layout.addRow('姓名', QLineEdit())
    layout.addRow('地址', QLineEdit())
    # 设置选项卡的小标题与布局方式
    GWidget.setTabText(0, '联系方式')
    GWidget.setLayout(layout)

def tab2UI(GWidget):
    # zhu表单布局，次水平布局
    layout = QFormLayout()
    sex = QHBoxLayout()

    # 水平布局添加单选按钮
    sex.addWidget(QRadioButton('男'))
    sex.addWidget(QRadioButton('女'))

    # 表单布局添加控件
    layout.addRow(QLabel('性别'), sex)
    layout.addRow('生日', QLineEdit())

    # 设置标题与布局
    GWidget.setTabText(1, '个人详细信息')
    GWidget.tab2.setLayout(layout)

def tab3UI(GWidget):
    # 水平布局
    layout = QHBoxLayout()

    # 添加控件到布局中
    layout.addWidget(QLabel('科目'))
    layout.addWidget(QCheckBox('物理'))
    layout.addWidget(QCheckBox('高数'))

    # 设置小标题与布局方式
    GWidget.setTabText(2, '教育程度')
    GWidget.tab3.setLayout(layout)


