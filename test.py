from PyQt5.QtGui import QMovie, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt, QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建静态和动态图片
        self.static_img = QLabel(self)
        self.static_img.setPixmap(QPixmap("icon/phone.png"))
        self.static_img.setGeometry(150,150,256,256)
        self.dynamic_img = QLabel(self)
        self.dynamic_img.setGeometry(self.static_img.geometry())

        # 创建计时器，用于切换图片
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.switch_image)

        # 创建计时器，用于长按检测
        self.long_press_timer = QTimer(self)
        self.long_press_timer.timeout.connect(self.long_press_detected)

        # 设置窗口属性
        self.setGeometry(100, 100, 1000, 1000)
        self.setWindowTitle("Image Switcher")
        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 鼠标左键按下，开始播放动态图片
            self.static_img.hide()
            self.dynamic_img.show()
            self.timer.start(100)  # 设置每100毫秒切换一次图片
            self.long_press_timer.start(200)  # 设置长按计时器为2秒

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 鼠标左键松开，停止播放动态图片和长按检测
            self.timer.stop()
            self.dynamic_img.hide()
            self.static_img.show()
            self.long_press_timer.stop()
            self.long_press_timer.start() # 重置长按计时器

    def switch_image(self):
        # 切换图片
        if self.dynamic_img.pixmap() is None:
            self.dynamic_img.setMovie(QMovie("icon/play.gif"))
            self.dynamic_img.movie().start()
        else:
            self.dynamic_img.clear()

    def long_press_detected(self):
        # 长按检测到，切换到GIF图片
        self.static_img.hide()
        self.dynamic_img.show()
        self.dynamic_img.setMovie(QMovie("icon/play.gif"))
        self.dynamic_img.movie().start()
        self.timer.stop()
        self.long_press_timer.stop()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec_()
