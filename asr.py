from PyQt5 import QtWidgets
from asrInterface import Ui_MainWindow
import sys
import threading
import speech_recognition as sr
import subprocess

class myWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(myWindow, self).__init__()
        self.myCommand = " "
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.pressed.connect(self.start_listening)

    def start_listening(self):
        # 开启线程
        self.thread = threading.Thread(target=self.listen_audio)
        self.thread.start()

    def exit_program(self):
        QtWidgets.QApplication.quit()  # 退出程序

    def listen_audio(self):
        self.ui.label.setText("I'm listening:")
        r = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        # 将识别结果发送到 GUI 中
        self.myCommand = r.recognize_google(audio)
        self.update_label()
        if 'setting' in self.myCommand: # os.system('start ms-settings:')
            subprocess.Popen('start ms-settings:', shell=True)
        elif 'note' in self.myCommand:
            subprocess.Popen(['notepad.exe'], shell=True)
        elif "bye" in self.myCommand:
            self.exit_program()
        elif 'name' in self.myCommand:
            self.ui.label_5.setText("I'm your assistant, Momoko")
        else:
            self.ui.label_5.setText("sorry, I don't understand")

    def update_label(self):
        # 更新 GUI 中的 Label 显示
        self.ui.label.setText(self.myCommand)

app = QtWidgets.QApplication([])
application = myWindow()
application.show()
sys.exit(app.exec())
