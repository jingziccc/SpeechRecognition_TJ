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
        r = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        # 将识别结果发送到 GUI 中
        self.myCommand = r.recognize_sphinx(audio)
        self.update_label()
        if 'setting' in self.myCommand: # os.system('start ms-settings:')
            subprocess.Popen('start ms-settings:', shell=True)
        elif 'notepad' in self.myCommand:
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

# from PyQt5 import QtWidgets, QtGui, QtCore
# from asrInterface import Ui_MainWindow
# import sys
# import threading
# import speech_recognition as sr
# import requests
# import subprocess
#
# class myWindow(QtWidgets.QMainWindow):
#
#     def __init__(self):
#         super(myWindow, self).__init__()
#         self.myCommand = " "
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#
#         # 设置Google Cloud Speech API的API密钥
#         self.GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"path/to/credentials.json"
#
#         # 将按钮事件连接到槽函数
#         self.ui.pushButton.clicked.connect(self.start_recognition)
#
#     def start_recognition(self):
#         # 启动一个线程，以避免冻结GUI
#         threading.Thread(target=self.listen_audio).start()
#
#     def listen_audio(self):
#         r = sr.Recognizer()
#         mic = sr.Microphone()
#         with mic as source:
#             r.adjust_for_ambient_noise(source)
#
#             # 使用Google Cloud Speech API进行在线语音识别
#             audio = r.listen(source)
#             url = "https://speech.googleapis.com/v1/speech:recognize?key=YOUR_API_KEY"
#             data = {
#                 "config": {
#                     "encoding": "LINEAR16",
#                     "languageCode": "en-US",
#                 },
#                 "audio": {
#                     "content": audio.get_raw_data(convert_rate=16000, convert_width=2),
#                 }
#             }
#             headers = {"Content-Type": "application/json"}
#             response = requests.post(url, json=data, headers=headers)
#
#         # 将识别结果发送到 GUI 中
#         self.myCommand = response.json()["results"][0]["alternatives"][0]["transcript"]
#         self.update_label()
#
#         # 如果识别结果包含"open settings"，则打开Windows 10的设置应用程序
#         if "open settings" in self.myCommand.lower():
#             subprocess.Popen(["start", "ms-settings:"])
#
#         # 如果识别结果包含"open notepad"，则打开Windows 10的记事本应用程序
#         elif "open notepad" in self.myCommand.lower():
#             subprocess.Popen(["start", "notepad.exe"])
#
#         # 如果识别结果包含"byebye"，则关闭应用程序
#         elif "byebye" in self.myCommand.lower():
#             QtWidgets.QApplication.quit()
#
#     def update_label(self):
#         # 更新 GUI 中的标签
#         self.ui.label.setText(self.myCommand)
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#     application = myWindow()
#     application.show()
#     sys.exit(app.exec_())
