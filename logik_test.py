"""
    Импорт библиотек для работы со времененм и звуком
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from disain2 import Ui_TitileBudilnic
from playsound import playsound
import time
import datetime


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


sound = "C:\\Users\\Stuffing\\PycharmProjects\\Firstproject\\miniproject\\mp3\\night-owl.mp3"

day_need, moth_need, hour_need, minutes_need = ui.lineEdit.text(), ui.lineEdit_2.text(), \
                                               ui.lineEdit_3.text(), ui.lineEdit_4.text()



def FunctionAlgo():
    while True:
        """
            Уменьшение нагрузки на программу расчет разныцы текущего времени и необходимого
        в секундах для отправки программы в ожидание.
        """
        date_now = datetime.datetime.now()

        time_difference = ((int(day_need) - date_now.day) * 86400) + (
                (int(moth_need) - date_now.month) * 30 * 86400) + (
                                  (int(hour_need) - date_now.hour) * 3600) + (
                                  (int(minutes_need) - date_now.minute) * 60) - date_now.second

        if time_difference > 0:
            print(f"До будильника осталось {time_difference // 60} минут {time_difference % 60} секунд")
            time.sleep(time_difference)
        else:
            if int(day_need) == date_now.day and int(moth_need) == date_now.month \
                    and int(hour_need) == date_now.hour and int(minutes_need) == date_now.minute:
                """
                    Цикл для увеличение времени проигрывания музыки до минуты
                """
                for _ in range(5):
                    playsound(sound)
                print(f"Будильник повториться через {int(time_repeat) * 60} секунд ")
                rerun(time_repeat, count_repeat)
            break
