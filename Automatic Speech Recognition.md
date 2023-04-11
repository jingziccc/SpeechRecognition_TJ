# Automatic Speech Recognition

<h2 style="text-align:right">2152831 陈峥海</h2>

## 1.programming environment and functions

### 1.1 Environment

+ python interpreter: python3.7

+ package: SpeechRecognition   pocketsphinx  PyAudio  PyQt5

+ IDE: PyCharm

  ![image-20230411160109332](E:\用户交互技术\assets\image-20230411160109332.png)

### 1.2 Functions

+ open settings
+ open notepad
+ play music
+ answer her name
+ say 'bye' and close

## 2.The modifications to GUI and the codes

### 2.1 GUI

​		The original graphical interface was crowded, and there were no buttons for speech recognition. In order to improve the user experience, I added a button that will start speech recognition when we press it. At the same time, the identified text will be displayed.

​		In addition to displaying what I said, I also set up a TAB for the man-machine conversation. There is no API yet and it can only be used for simple set conversations. After that, the ChatGPT API will be plugged in for human-machine conversation.

​		Here's the picture of the GUI.

​		<img src="C:\Users\czh26\AppData\Roaming\Typora\typora-user-images\image-20230411154422371.png" alt="image-20230411154422371" style="zoom:80%;" /><img src="C:\Users\czh26\AppData\Roaming\Typora\typora-user-images\image-20230411154639070.png" alt="image-20230411154639070" style="zoom: 80%;" />

<img src="C:\Users\czh26\AppData\Roaming\Typora\typora-user-images\image-20230411154755409.png" alt="image-20230411154755409" style="zoom:80%;" /><img src="C:\Users\czh26\AppData\Roaming\Typora\typora-user-images\image-20230411154850940.png" alt="image-20230411154850940" style="zoom:80%;" />

### 2.2 code

​		At the beginning, the definition of label was very confusing, so I sorted out the definition of label and redefined it to make it more readable.

​		At the same time, I set up a button to start and end the conversation. When the button is long pressed, the recognition begins; Recognition ends when the button is released.

​		Here's the code of the GUI.

```python
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.window_width = 500
        self.window_height = 700
        self.label_width = self.window_width * (4 / 5)
        self.label_height = self.window_height / 10

        MainWindow.resize(self.window_width, self.window_height)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)

        # 按钮控件设置
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(self.window_width / 2 - 60, self.window_height - 100, 120, 40))
        self.pushButton.setText("Start Listening")
        self.pushButton.setFont(font)
        self.pushButton.pressed.connect(self.start_listening)
        self.pushButton.released.connect(self.stop_listening)
        self.pushButton.setStyleSheet("background-color: rgb(173, 216, 230);")
        # label控件设置
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 250, 201, 21))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.labels = [self.label_2, self.label_3, self.label_4, self.label_5]

        self.voiceFig = QtWidgets.QLabel(self.centralwidget)
        self.voiceFig.setGeometry(QtCore.QRect(self.window_width / 2 - 130, 0, 100, 121))
        self.voiceFig.setText("")
        self.gif = QMovie("icon/voice.gif")
        self.voiceFig.setMovie(self.gif)
        self.gif.start()
        self.voiceFig.setFixedSize(self.gif.frameRect().size() / 2.5)
        self.voiceFig.setScaledContents(True)
        self.voiceFig.setObjectName("voiceFig")

        for idx, label in enumerate(self.labels):
            label.setGeometry(QtCore.QRect(60, 280 + idx * 70, self.label_width, 50))
            label.setFont(font)
            label.setStyleSheet("color: rgb(0, 117, 210);")
            label.setWordWrap(True)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(self.window_width / 2 - 120,  (self.window_height - self.label_height) / 8 + 80, self.label_width, 60))
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 117, 210);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voice Assistant"))
        self.label_3.setText(_translate("MainWindow", "1. Play music by saying \"Play music\""))
        self.label_2.setText(_translate("MainWindow", "You can:"))
        self.label.setText(_translate("MainWindow", "Hi! How can I help?"))
        self.label_4.setText(_translate("MainWindow", "2. Take some notes by saying \"Open Notepad\""))
        self.label_5.setText(_translate("MainWindow", " "))

    def start_listening(self):
        # 在这里编写开始录音的代码
        print("开始录音")

    def stop_listening(self):
        # 在这里编写停止录音的代码
        print("停止录音")
```

​		Because of speech_recognition is blocking, meaning that the program will wait until the audio input is completed. You can try placing the listen method in a separate thread to avoid blocking the main thread and allow the GUI to respond normally. I use Python's built-in threading module to enable threads.

```python
from PyQt5 import QtWidgets
from asrInterface import Ui_MainWindow
import sys
import threading
import speech_recognition as sr
import subprocess
import os
import win32api


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
        self.myCommand = self.myCommand.lower()
        if 'setting' in self.myCommand:
            subprocess.Popen('start ms-settings:', shell=True)
        elif 'notepad' in self.myCommand:
            subprocess.Popen(['notepad.exe'], shell=True)
        elif "bye" in self.myCommand:
            self.exit_program()
        elif 'name' in self.myCommand or 'who' in self.myCommand:
            self.ui.label_5.setText("I'm your assistant, Momoko")
        elif 'play music' in self.myCommand:
            win32api.ShellExecute(0, 'open', 'music.wav', '', '', 1)
        else:
            self.ui.label_5.setText("sorry, I don't understand")
        self.update_label()  # 更新 label 显示


    def update_label(self):
        # 更新 GUI 中的 Label 显示
        self.ui.label.setText(self.myCommand)

app = QtWidgets.QApplication([])
application = myWindow()
application.show()
sys.exit(app.exec())

```

## 3.The accuracy of speech recognition

### 3.1 The accuracy

​		At the beginning, I used offline speech recognition package==**(r.recognize_sphinx())**==, and the recognition efficiency was very low. It works because it is translated word by word, without context. After using Google api(==**r.recognize_google**==) to realize online real-time translation, the recognition efficiency increased by nearly 90%.

| speaking                 | sphinx   | google   |
| ------------------------ | -------- | -------- |
| I want to eat apple * 10 | 2/10=20% | 9/10=90% |
| open notepad for me * 10 | 1/10=10% | 8/10=80% |
| who are you * 10         | 3/10=30% | 9/10=90% |

### 3.2 Improvement

1. As you can see from the table above, you can access an online speech recognition API to improve accuracy.
2. At the same time, recognition accuracy improves when my speech is long enough.

3. In a relatively quiet environment, in standard English.