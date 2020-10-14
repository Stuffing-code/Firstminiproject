import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from disain2 import Ui_TitileBudilnic
from playsound import playsound
import time
import datetime

# create app
app = QtWidgets.QApplication(sys.argv)

# init

TitileBudilnic = QtWidgets.QDialog()
ui = Ui_TitileBudilnic()
ui.setupUi(TitileBudilnic)
TitileBudilnic.show()


# Hook Logik
sound = "C:\\Users\\Stuffing\\PycharmProjects\\Firstproject\\miniproject\\mp3\\night-owl.mp3"

def rerun(repeat=5, count=1):
    """
    функция на повтор будильника
    :param repeat: через сколько повторят будильник
    :param count: количество повторений
    :return: проигрывает мелодию
    """

    for _ in range(count):
        time.sleep(repeat * 60)
        for _ in range(5):
            return playsound(sound)


def sound_alarm():
    for _ in range(1):
        playsound(sound)


def OpenClick():
    day_need, moth_need, hour_need, minutes_need = ui.lineEdit.text(), ui.lineEdit_2.text(), \
                                                   ui.lineEdit_3.text(), ui.lineEdit_4.text()
    date_now = datetime.datetime.now()

    time_difference = ((int(day_need) - date_now.day) * 86400) + (
            (int(moth_need) - date_now.month) * 30 * 86400) + (
                              (int(hour_need) - date_now.hour) * 3600) + (
                              (int(minutes_need) - date_now.minute) * 60) - date_now.second

    ui.label_6.setText(f"Alarm clock set {day_need}.{moth_need} {hour_need}:{minutes_need}")
    ui.label_5.setText(f"Time left {time_difference // 60} minutes \n {time_difference % 60} second")

def start_sound_alarm():
    day_need, moth_need, hour_need, minutes_need = ui.lineEdit.text(), ui.lineEdit_2.text(), \
                                                   ui.lineEdit_3.text(), ui.lineEdit_4.text()
    while True:
        date_now = datetime.datetime.now()

        time_difference = ((int(day_need) - date_now.day) * 86400) + (
                (int(moth_need) - date_now.month) * 30 * 86400) + (
                                  (int(hour_need) - date_now.hour) * 3600) + (
                                  (int(minutes_need) - date_now.minute) * 60) - date_now.second
        if time_difference > 0:
            time.sleep(time_difference)
            sound_alarm()
            break
        else:
            sound_alarm()




ui.pushButton.clicked.connect(OpenClick)
ui.pushButton_2.clicked.connect(start_sound_alarm)

# main loop
sys.exit(app.exec_())
