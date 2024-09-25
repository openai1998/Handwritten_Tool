import sys
import os
import logging
import random
import shutil
from PySide6.QtCore import Signal, QThread, QObject, QCoreApplication
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PIL import Image, ImageFont, ImageQt
from handright import Template, handwrite
import time

from ui import *

# 设置日志
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("handwrite_debug.log"),
                        logging.StreamHandler()
                    ])

# 创建临时文件夹
TEMP_DIR = "./temp_preview"
if not os.path.exists(TEMP_DIR):
    os.mkdir(TEMP_DIR)

class ImageProcessor(QObject):
    finished = Signal()
    preview_ready = Signal(object)
    progress = Signal(int)

    def __init__(self, background_path, angle=None, text=None, template=None):
        super().__init__()
        self.background_path = background_path
        self.angle = angle
        self.text = text
        self.template = template
        self.stop_flag = False
        logging.debug(f"图像处理器初始化，背景：{background_path}，角度：{angle}")

    def rotate_image(self):
        logging.debug(f"正在旋转图像：{self.background_path}，角度：{self.angle}")
        if os.path.exists(self.background_path):
            image = Image.open(self.background_path)
            rotated_image = image.rotate(self.angle, expand=True)
            rotated_image.save(self.background_path)
            self.preview_ready.emit(rotated_image)
            logging.info(f"图像已旋转并保存：{self.background_path}")
        else:
            logging.error(f"未找到背景图像：{self.background_path}")
        self.finished.emit()

    def generate_preview(self):
        logging.debug("正在生成预览")
        if self.text and self.template:
            images = list(handwrite(self.text, self.template))
            total = len(images)
            logging.info(f"已生成 {total} 张预览图像")
            for i, image in enumerate(images):
                if self.stop_flag:
                    break
                filename = os.path.join(TEMP_DIR, f"preview_{i}.png")
                image.save(filename)
                self.preview_ready.emit(image)
                self.progress.emit(int((i + 1) / total * 100))
                QCoreApplication.processEvents()
            logging.info(f"预览图像已保存在 {TEMP_DIR}")
        else:
            logging.warning("无法生成预览：缺少文本或模板")
        self.finished.emit()

    def stop(self):
        self.stop_flag = True

class mainwindow(QMainWindow, Ui_Form):
    sendmsg = Signal()

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.font_selection_button.clicked.connect(lambda: self.font.setText(getfile()))
        self.background_selection_button.clicked.connect(lambda: self.background.setText(getfile()))
        self.preview_button.clicked.connect(self.preview)
        self.export_button.clicked.connect(self.export)
        self.save_button.clicked.connect(self.save)
        self.load_utton.clicked.connect(self.load)
        self.sendmsg.connect(self.msg)
        self.rotate_left_button.clicked.connect(lambda: self.start_image_processing(-90))
        self.rotate_right_button.clicked.connect(lambda: self.start_image_processing(90))
        self.current_template = None
        logging.info("主窗口已初始化")

    def start_image_processing(self, angle):
        logging.debug(f"开始图像处理，角度：{angle}")
        self.thread = QThread()
        self.image_processor = ImageProcessor(self.background.text(), angle=angle)
        self.image_processor.moveToThread(self.thread)
        self.thread.started.connect(self.image_processor.rotate_image)
        self.image_processor.preview_ready.connect(self.update_preview)
        self.image_processor.finished.connect(self.thread.quit)
        self.image_processor.finished.connect(self.image_processor.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

    def start_preview_generation(self):
        logging.debug("开始生成预览")
        self.thread = QThread()
        self.image_processor = ImageProcessor(self.background.text(), text=self.pending_text.toPlainText(), template=self.current_template)
        self.image_processor.moveToThread(self.thread)
        self.thread.started.connect(self.image_processor.generate_preview)
        self.image_processor.preview_ready.connect(self.update_preview)
        self.image_processor.progress.connect(self.update_progress)
        self.image_processor.finished.connect(self.thread.quit)
        self.image_processor.finished.connect(self.image_processor.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(lambda: self.preview_button.setEnabled(True))
        self.thread.start()

    def update_preview(self, image):
        logging.debug("更新预览图像")
        image = image.convert("RGBA")
        pixmap = ImageQt.toqpixmap(image)
        self.preview_area.setScaledContents(True)
        self.preview_area.setPixmap(pixmap)
        QCoreApplication.processEvents()

    def update_progress(self, value):
        logging.debug(f"更新进度：{value}%")
        self.progress_bar.setValue(value)
        QCoreApplication.processEvents()

    def msg(self):
        logging.info("导出完成，显示消息")
        QMessageBox.information(self, "完成", "已导出图片到output目录下")

    def save(self):
        logging.debug("保存设置")
        file_path = savefile()
        if file_path != "":
            file_text = "%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s" % (
                self.red.text(), self.green.text(), self.blue.text(), self.font.text(),
                self.background.text(), self.word_spacing.text(), self.word_spacing_sigma.text(), self.line_spacing.text(),
                self.line_spacing_sigma.text(), self.font_size.text(), self.font_size_sigma.text(), self.perturb_x_sigma.text(),
                self.perturb_y_sigma.text(), self.perturb_theta_sigma.text(), self.top_margin.text(), self.left_margin.text(),
                self.right_margin.text(), self.bottom_margin.text())
            with open(file=file_path, mode='w', encoding='utf-8') as file:
                file.write(file_text)
            logging.info(f"设置已保存到：{file_path}")

    def load(self):
        logging.debug("加载设置")
        file_path = getfile()
        if file_path != "":
            with open(file=file_path, mode='r', encoding='utf-8') as file:
                data = file.read().split('\n')
            self.red.setText(data[0])
            self.green.setText(data[1])
            self.blue.setText(data[2])
            self.font.setText(data[3])
            self.background.setText(data[4])
            self.word_spacing.setText(data[5])
            self.word_spacing_sigma.setValue(int(data[6]))
            self.line_spacing.setText(data[7])
            self.line_spacing_sigma.setValue(int(data[8]))
            self.font_size.setText(data[9])
            self.font_size_sigma.setValue(int(data[10]))
            self.perturb_x_sigma.setValue(int(data[11]))
            self.perturb_y_sigma.setValue(int(data[12]))
            self.perturb_theta_sigma.setValue(float(data[13]))
            self.top_margin.setText(data[14])
            self.left_margin.setText(data[15])
            self.right_margin.setText(data[16])
            self.bottom_margin.setText(data[17])
            logging.info(f"设置已从以下位置加载：{file_path}")

    def preview(self):
        logging.debug("开始预览过程")
        if self.font.text() == "" or self.word_spacing.text() == "" or self.bottom_margin.text() == "":
            QMessageBox.information(self, "检查参数", "请检查参数是否完整")
            logging.warning("预览参数不完整")
        elif self.pending_text.toPlainText() == "":
            QMessageBox.information(self, "!!!", "未输入要处理的文字")
            logging.warning("预览没有输入文本")
        elif not os.path.exists(self.font.text()):
            QMessageBox.information(self, "路径错误", "字体指定的路径不存在")
            logging.error(f"未找到字体文件：{self.font.text()}")
        elif not os.path.exists(self.background.text()):
            QMessageBox.information(self, "路径错误", "背景指定的路径不存在")
            logging.error(f"未找到背景图像：{self.background.text()}")
        elif int(self.line_spacing.text()) <= int(self.font_size.text()):
            QMessageBox.warning(self, "参数错误", "行间距必须大于字体大小")
            logging.warning("行间距不大于字体大小")
        else:
            self.preview_button.setEnabled(False)
            self.current_template = self.get_template()
            logging.info(f"已为预览创建模板：{self.current_template}")
            self.progress_bar.setValue(0)
            self.start_preview_generation()

    def export(self):
        logging.debug("开始导出过程")
        if not os.path.exists(TEMP_DIR) or not os.listdir(TEMP_DIR):
            QMessageBox.information(self, "错误", "请先预览后再导出")
            logging.warning("尝试在预览之前导出")
            return
        
        if not os.path.exists("./output"):
            os.mkdir("./output")
        self.export_button.setEnabled(False)
        try:
            timestamp = time.strftime("%Y%m%d%H%M%S")
            for filename in os.listdir(TEMP_DIR):
                src = os.path.join(TEMP_DIR, filename)
                dst = f"./output/{timestamp}_{filename}"
                shutil.copy(src, dst)
                logging.info(f"图像已导出：{dst}")
            self.sendmsg.emit()
        except Exception as e:
            QMessageBox.critical(self, "错误", f"导出过程中发生错误：{str(e)}")
            logging.exception("导出过程中发生错误")
        finally:
            self.export_button.setEnabled(True)

    def get_template(self):
        logging.debug("创建模板")
        font_size = int(self.font_size.text())
        line_spacing = int(self.line_spacing.text())
        
        # 确保行间距至少比字体大小大 1 像素
        if line_spacing <= font_size:
            line_spacing = font_size + 1
            logging.warning(f"已调整行间距为 {line_spacing} 以满足 handright 要求")

        try:
            background = Image.open(self.background.text())
            font = ImageFont.truetype(self.font.text(), size=font_size)
        except Exception as e:
            logging.error(f"加载背景或字体时出错: {str(e)}")
            QMessageBox.critical(self, "错误", f"加载背景或字体时出错: {str(e)}")
            return None

        # 生成全局随机种子
        global_seed = random.randint(0, 100000)
        logging.info(f"使用全局随机种子: {global_seed}")
        
        # 使用全局种子设置随机状态
        random.seed(global_seed)

        template = Template(
            background=background,
            font=font,
            line_spacing=line_spacing,
            fill=(int(self.red.text()), int(self.green.text()), int(self.blue.text())),
            left_margin=int(self.left_margin.text()),
            top_margin=int(self.top_margin.text()),
            right_margin=int(self.right_margin.text()),
            bottom_margin=int(self.bottom_margin.text()),
            word_spacing=int(self.word_spacing.text()),
            line_spacing_sigma=int(self.line_spacing_sigma.text()),
            font_size_sigma=int(self.font_size_sigma.text()),
            word_spacing_sigma=int(self.word_spacing_sigma.text()),
            start_chars='"([<',
            end_chars='，。',
            perturb_x_sigma=int(self.perturb_x_sigma.text()),
            perturb_y_sigma=int(self.perturb_y_sigma.text()),
            perturb_theta_sigma=float(self.perturb_theta_sigma.text())
        )
        logging.info(f"已创建模板：{template}")
        return template

def getfile():
    logging.debug("正在打开文件选择对话框")
    q = QFileDialog.getOpenFileName()
    logging.info(f"已选择文件: {q[0]}")
    return q[0]

def savefile():
    logging.debug("正在打开文件保存对话框")
    q = QFileDialog.getSaveFileName()
    logging.info(f"已选择保存位置: {q[0]}")
    return q[0]

def cleanup():
    logging.info("正在清理临时文件")
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)
        logging.info(f"临时目录已删除: {TEMP_DIR}")

if __name__ == "__main__":
    logging.info("启动应用程序")
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    app.aboutToQuit.connect(cleanup)
    sys.exit(app.exec())