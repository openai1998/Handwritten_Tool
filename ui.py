from PySide6 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        # 设置窗口对象的名称为"Form"，便于在调试和对象查找时识别。
        Form.setObjectName("Form")
        # 设置窗口为非模态窗口，该窗口打开时，用户仍可以与父窗口或其他窗口交互。
        Form.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        # 启用该窗口，不隐藏
        Form.setEnabled(True)
        # 窗口大小
        Form.resize(848, 592)
        # 大小调整策略
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(848, 592))
        Form.setMaximumSize(QtCore.QSize(848, 592))
        # 设置窗口图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./ui/3d.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        # 设置窗口透明度
        Form.setWindowOpacity(0.98)
        # 设置窗口描述，用于无障碍
        Form.setAccessibleDescription("")
        # 设置窗口的布局方向，汉语言为从左到右，从上到下。
        Form.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        # 样式表
        Form.setStyleSheet("font: 10pt 楷体; border-radius: 3px;")

        # 待处理文本编辑器
        self.pending_text = QtWidgets.QTextEdit(Form)
        self.pending_text.setGeometry(QtCore.QRect(430, 30, 411, 221))
        self.pending_text.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pending_text.setAutoFillBackground(False)
        self.pending_text.setStyleSheet("border-radius: 30px;")
        self.pending_text.setObjectName("textEdit")

        # 字体选择路径
        self.font = QtWidgets.QLineEdit(Form)
        self.font.setGeometry(QtCore.QRect(480, 280, 311, 20))
        self.font.setText("")
        self.font.setObjectName("lineEdit")

        # 字体选择按钮
        self.font_selection_button = QtWidgets.QPushButton(Form)
        self.font_selection_button.setGeometry(QtCore.QRect(792, 281, 45, 18))
        self.font_selection_button.setStyleSheet("background-color: rgb(221, 255, 235);")
        self.font_selection_button.setObjectName("pushButton")
        
        # 背景选择按钮
        self.background_selection_button = QtWidgets.QPushButton(Form)
        self.background_selection_button.setGeometry(QtCore.QRect(792, 311, 45, 18))
        self.background_selection_button.setStyleSheet("background-color: rgb(221, 255, 235);")
        self.background_selection_button.setObjectName("pushButton_2")

        # 背景选择路径
        self.background = QtWidgets.QLineEdit(Form)
        self.background.setGeometry(QtCore.QRect(480, 310, 311, 20))
        self.background.setText("")
        self.background.setObjectName("lineEdit_2")
        
        # 上边距文本框
        self.top_margin = QtWidgets.QLineEdit(Form)
        self.top_margin.setGeometry(QtCore.QRect(720, 357, 61, 24))
        self.top_margin.setText("")
        self.top_margin.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.top_margin.setObjectName("top_margin")
        
        # 下边距文本框
        self.bottom_margin = QtWidgets.QLineEdit(Form)
        self.bottom_margin.setGeometry(QtCore.QRect(720, 431, 61, 24))
        self.bottom_margin.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.bottom_margin.setObjectName("lineEdit_4")
        
        # 左边距文本框
        self.left_margin = QtWidgets.QLineEdit(Form)
        self.left_margin.setGeometry(QtCore.QRect(697, 380, 24, 51))
        self.left_margin.setText("")
        self.left_margin.setObjectName("lineEdit_5")

        # 右边距文本框
        self.right_margin = QtWidgets.QLineEdit(Form)
        self.right_margin.setGeometry(QtCore.QRect(780, 380, 24, 51))
        self.right_margin.setObjectName("lineEdit_6")

        # 字水平边距设置框
        self.word_spacing_sigma = QtWidgets.QSpinBox(Form)
        self.word_spacing_sigma.setGeometry(QtCore.QRect(600, 360, 51, 20))
        self.word_spacing_sigma.setObjectName("spinBox")

        # 字水平边距文本框
        self.word_spacing = QtWidgets.QLineEdit(Form)
        self.word_spacing.setGeometry(QtCore.QRect(514, 360, 74, 20))
        self.word_spacing.setObjectName("lineEdit_7")

        # 字竖直边距文本框
        self.line_spacing = QtWidgets.QLineEdit(Form)
        self.line_spacing.setGeometry(QtCore.QRect(514, 400, 74, 20))
        self.line_spacing.setObjectName("lineEdit_8")
        
        # 字竖直边距设置框
        self.line_spacing_sigma = QtWidgets.QSpinBox(Form)
        self.line_spacing_sigma.setGeometry(QtCore.QRect(600, 400, 51, 20))
        self.line_spacing_sigma.setObjectName("spinBox_2")
        
        # 字体大小文本框
        self.font_size = QtWidgets.QLineEdit(Form)
        self.font_size.setGeometry(QtCore.QRect(514, 440, 74, 20))
        self.font_size.setObjectName("lineEdit_9")
        
        # 字体大小设置框
        self.font_size_sigma = QtWidgets.QSpinBox(Form)
        self.font_size_sigma.setGeometry(QtCore.QRect(600, 440, 51, 20))
        self.font_size_sigma.setObjectName("spinBox_3")
        
        # 竖直笔画偏移设置框
        self.perturb_y_sigma = QtWidgets.QSpinBox(Form)
        self.perturb_y_sigma.setGeometry(QtCore.QRect(600, 520, 51, 20))
        self.perturb_y_sigma.setProperty("value", 4)
        self.perturb_y_sigma.setObjectName("spinBox_4")
        
        # 水平笔画偏移设置框
        self.perturb_x_sigma = QtWidgets.QSpinBox(Form)
        self.perturb_x_sigma.setGeometry(QtCore.QRect(600, 480, 51, 20))
        self.perturb_x_sigma.setProperty("value", 4)
        self.perturb_x_sigma.setObjectName("spinBox_5")
        
        # 笔画旋转设置框
        self.perturb_theta_sigma = QtWidgets.QDoubleSpinBox(Form)
        self.perturb_theta_sigma.setGeometry(QtCore.QRect(600, 560, 51, 20))
        self.perturb_theta_sigma.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.perturb_theta_sigma.setSingleStep(0.01)
        self.perturb_theta_sigma.setProperty("value", 0.05)
        self.perturb_theta_sigma.setObjectName("doubleSpinBox_6")

        # 旋转背景图按钮
        # 创建向左旋转按钮
        self.rotate_left_button = QtWidgets.QPushButton(Form)
        self.rotate_left_button.setGeometry(QtCore.QRect(680, 460, 75, 23))
        self.rotate_left_button.setStyleSheet("background-color: rgb(221, 255, 235);")
        self.rotate_left_button.setObjectName("rotate_left_button")
        # 创建向右旋转按钮
        self.rotate_right_button = QtWidgets.QPushButton(Form)
        self.rotate_right_button.setGeometry(QtCore.QRect(760, 460, 75, 23))
        self.rotate_right_button.setStyleSheet("background-color: rgb(221, 255, 235);")
        self.rotate_right_button.setObjectName("rotate_right_button")

        # 预览按钮
        # 创建预览按钮
        self.preview_button = QtWidgets.QPushButton(Form)
        # 设置按钮的位置和大小（x=700, y=500, 宽度=101, 高度=31）
        self.preview_button.setGeometry(QtCore.QRect(700, 500, 101, 31))
        # 设置按钮的背景颜色为浅绿色（RGB: 157, 220, 128）
        self.preview_button.setStyleSheet("background-color: rgb(157, 220, 128);")
        # 设置按钮的对象名称，用于在代码中引用此按钮
        self.preview_button.setObjectName("pushButton_3")

        # 导出按钮
        self.export_button = QtWidgets.QPushButton(Form)
        self.export_button.setGeometry(QtCore.QRect(700, 540, 101, 31))
        self.export_button.setStyleSheet("background-color: rgb(157, 220, 128);")
        self.export_button.setObjectName("pushButton_5")

        # 预览区域
        self.preview_area = QtWidgets.QLabel(Form)
        self.preview_area.setGeometry(QtCore.QRect(3, 1, 420, 593))
        self.preview_area.setText("")
        self.preview_area.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.preview_area.setObjectName("label_11")

        # 主界面（除所有按钮、文本框之外的区域）
        self.main_interface = QtWidgets.QListView(Form)
        self.main_interface.setGeometry(QtCore.QRect(-5, -9, 861, 611))
        self.main_interface.setStyleSheet("background-image: url(./ui/night.png); color: rgb(11, 214, 255);")
        self.main_interface.setObjectName("listView")
        
        # 保存按钮
        self.save_button = QtWidgets.QPushButton(Form)
        self.save_button.setGeometry(QtCore.QRect(600, 334, 51, 23))
        self.save_button.setAutoFillBackground(False)
        self.save_button.setStyleSheet("background-color: rgb(221, 255, 235);")
        self.save_button.setObjectName("pushButton_4")
        
        # 载入按钮
        self.load_utton = QtWidgets.QPushButton(Form)
        self.load_utton.setGeometry(QtCore.QRect(514, 334, 74, 23))
        self.load_utton.setStyleSheet("background-color: rgb(221, 255, 235);")
        self.load_utton.setAutoDefault(False)
        self.load_utton.setObjectName("pushButton_6")
        
        # R文本框
        self.red = QtWidgets.QLineEdit(Form)
        self.red.setGeometry(QtCore.QRect(727, 259, 31, 20))
        self.red.setObjectName("lineEdit_10")
        
        # G文本框
        self.green = QtWidgets.QLineEdit(Form)
        self.green.setGeometry(QtCore.QRect(760, 259, 31, 20))
        self.green.setObjectName("lineEdit_11")
        self.blue = QtWidgets.QLineEdit(Form)
        
        # B文本框
        # 设置B文本框的位置和大小（坐标：793, 259，宽度：31，高度：20）
        self.blue.setGeometry(QtCore.QRect(793, 259, 31, 20))
        # 设置B文本框的对象名称为"lineEdit_12"
        self.blue.setObjectName("lineEdit_12")
        
        # 显示控件？
        self.main_interface.raise_()
        self.pending_text.raise_()
        self.font.raise_()
        self.font_selection_button.raise_()
        self.background_selection_button.raise_()
        self.background.raise_()
        self.top_margin.raise_()
        self.bottom_margin.raise_()
        self.left_margin.raise_()
        self.right_margin.raise_()
        self.word_spacing_sigma.raise_()
        self.word_spacing.raise_()
        self.line_spacing.raise_()
        self.line_spacing_sigma.raise_()
        self.font_size.raise_()
        self.font_size_sigma.raise_()
        self.perturb_y_sigma.raise_()
        self.perturb_x_sigma.raise_()
        self.perturb_theta_sigma.raise_()
        self.preview_button.raise_()
        self.export_button.raise_()
        self.preview_area.raise_()
        self.save_button.raise_()
        self.load_utton.raise_()
        self.red.raise_()
        self.green.raise_()
        self.blue.raise_()
        self.rotate_left_button.raise_()
        self.rotate_right_button.raise_()

        # 进度条
        # 创建一个进度条控件，并将其添加到主窗体Form中
        self.progress_bar = QtWidgets.QProgressBar(Form)
        # 设置进度条的位置和大小
        # 参数分别为：左上角x坐标，左上角y坐标，宽度，高度
        self.progress_bar.setGeometry(QtCore.QRect(480, 260, 200, 15))
        # 设置进度条的初始值为0
        self.progress_bar.setProperty("value", 0)
        # 设置进度条的对象名称，用于在代码中引用该控件
        self.progress_bar.setObjectName("progress_bar")

        # 添加种子输入框
        # 创建一个用于输入种子值的行编辑控件，并将其添加到主窗体Form中
        self.seed_input = QtWidgets.QLineEdit(Form)
        # 设置种子输入框的位置和大小
        # 参数分别为：左上角x坐标，左上角y坐标，宽度，高度
        self.seed_input.setGeometry(QtCore.QRect(720, 335, 61, 20))
        # 设置种子输入框的默认文本为"-1"
        self.seed_input.setText("-1")
        # 设置种子输入框的对象名称，用于在代码中引用该控件
        self.seed_input.setObjectName("seed_input")

        # 进度条提示
        self.progressbar = QtWidgets.QLabel(Form)
        self.progressbar.setGeometry(QtCore.QRect(430, 260, 60, 15))
        self.progressbar.setObjectName("progressbar")

        self.label_font = QtWidgets.QLabel(Form)
        self.label_font.setGeometry(QtCore.QRect(430, 280, 60, 20))
        self.label_font.setObjectName("label_font")

        self.label_background = QtWidgets.QLabel(Form)
        self.label_background.setGeometry(QtCore.QRect(430, 310, 60, 20))
        self.label_background.setObjectName("label_background")

        self.label_word_spacing = QtWidgets.QLabel(Form)
        self.label_word_spacing.setGeometry(QtCore.QRect(430, 360, 80, 20))
        self.label_word_spacing.setObjectName("label_word_spacing")

        self.label_line_spacing = QtWidgets.QLabel(Form)
        self.label_line_spacing.setGeometry(QtCore.QRect(430, 400, 80, 20))
        self.label_line_spacing.setObjectName("label_line_spacing")

        self.label_font_size = QtWidgets.QLabel(Form)
        self.label_font_size.setGeometry(QtCore.QRect(430, 440, 80, 20))
        self.label_font_size.setObjectName("label_font_size")

        self.label_perturb_x = QtWidgets.QLabel(Form)
        self.label_perturb_x.setGeometry(QtCore.QRect(430, 480, 120, 20))
        self.label_perturb_x.setObjectName("label_perturb_x")

        self.label_perturb_y = QtWidgets.QLabel(Form)
        self.label_perturb_y.setGeometry(QtCore.QRect(430, 520, 120, 20))
        self.label_perturb_y.setObjectName("label_perturb_y")

        self.label_perturb_theta = QtWidgets.QLabel(Form)
        self.label_perturb_theta.setGeometry(QtCore.QRect(430, 560, 120, 20))
        self.label_perturb_theta.setObjectName("label_perturb_theta")

        self.label_seed = QtWidgets.QLabel(Form)
        self.label_seed.setGeometry(QtCore.QRect(660, 335, 60, 20))
        self.label_seed.setObjectName("label_seed")

        self.label_rgb = QtWidgets.QLabel(Form)
        self.label_rgb.setGeometry(QtCore.QRect(700, 260, 60, 15))
        self.label_rgb.setObjectName("label_rgb")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "手写模拟"))
        self.pending_text.setPlaceholderText(_translate("Form", "本软件主要基于handwrite库开发，仅供学习交流。"))
        self.font.setAccessibleDescription(_translate("Form", "1111"))
        self.font_selection_button.setText(_translate("Form", "选择"))
        self.background_selection_button.setText(_translate("Form", "选择"))
        self.background.setAccessibleDescription(_translate("Form", "1111"))
        self.preview_button.setText(_translate("Form", "预览"))
        self.export_button.setText(_translate("Form", "导出"))
        self.save_button.setText(_translate("Form", "保存"))
        self.load_utton.setText(_translate("Form", "载入预设"))
        self.red.setText(_translate("Form", "0"))
        self.green.setText(_translate("Form", "0"))
        self.blue.setText(_translate("Form", "0"))
        self.rotate_left_button.setText(_translate("Form", "左旋转"))
        self.rotate_right_button.setText(_translate("Form", "右旋转"))
        self.seed_input.setPlaceholderText(_translate("Form", "输入种子值（-1表示随机）"))

        # 设置标签文本
        self.progressbar.setText(_translate("Form", "进度条"))
        self.label_font.setText(_translate("Form", "字体"))
        self.label_background.setText(_translate("Form", "背景"))
        self.label_word_spacing.setText(_translate("Form", "字水平间距"))
        self.label_line_spacing.setText(_translate("Form", "字竖直间距"))
        self.label_font_size.setText(_translate("Form", "字体大小"))
        self.label_perturb_x.setText(_translate("Form", "水平笔画位移"))
        self.label_perturb_y.setText(_translate("Form", "竖直笔画位移"))
        self.label_perturb_theta.setText(_translate("Form", "笔画旋转"))
        self.label_seed.setText(_translate("Form", "种子值"))
        self.label_rgb.setText(_translate("Form", "RGB"))