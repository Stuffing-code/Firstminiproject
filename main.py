"""
    Первый тестовый проект
"""
import time, datetime
from playsound import playsound

"""
    Функция для повтора будильника
"""


def rerun(time_repeat, count):
    for _ in range(count):
        time.sleep(time_repeat * 60)
        for _ in range(3):
            return playsound(sound)


def difference():
    pass


sound = "C:\\Users\\Stuffing\\PycharmProjects\\Firstproject\\miniproject\\mp3\\night-owl.mp3"
date_now = datetime.datetime.now()
time_alarm = input("Введите день, месяц и точное время будильника: ").split()
count_repeat = int(input("Сколько раз повторить: "))
time_repeat = float(input("Через сколько минут повторить: "))
"""
    Уменьшение нагрузки на программу расчет разныцы текущего времени и необходимого
в секундах для отправки программы в ожидание.
"""
time_difference = ((int(time_alarm[0]) - date_now.day) * 86400)\
                  + ((int(time_alarm[1]) - date_now.month) * 30 * 86400) \
                  + ((int(time_alarm[2]) - date_now.hour) * 3600) \
                  + ((int(time_alarm[3]) - date_now.minute) * 60) - date_now.second
while True:
    if time_difference > 0:
        print(f"До будильника осталось {time_difference // 60} минут {time_difference % 60} секунд")
        time.sleep(time_difference)
        """
            Обновление времени текущего и расчет разницы времени
        """
        date_now = datetime.datetime.now()
        time_difference = ((int(time_alarm[0]) - date_now.day) * 86400) + (
                (int(time_alarm[1]) - date_now.month) * 30 * 86400) \
                          + ((int(time_alarm[2]) - date_now.hour) * 3600) \
                          + ((int(time_alarm[3]) - date_now.minute) * 60) - date_now.second
    else:
        if int(time_alarm[0]) == date_now.day and int(time_alarm[1]) == date_now.month \
                and int(time_alarm[2]) == date_now.hour and int(time_alarm[3]) == date_now.minute:
            """
                Цикл для увеличение времени проигрывания музыки
            """
            for i in range(5):
                playsound(sound)
            print(f"Будильник повториться через {int(time_repeat) * 60} секунд ")
            rerun(time_repeat, count_repeat)
        break
