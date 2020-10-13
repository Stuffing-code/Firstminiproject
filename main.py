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
        return (f"Slept for {int(time_repeat)} "
                f"min {int((time_repeat * 60) % 60)} second")


def difference():
    pass


sound = "C:\\Users\\Stuffing\\PycharmProjects\\Firstproject\\miniproject\\mp3\\night-owl.mp3"
date_now = datetime.datetime.now()
time_alarm = input("Введите день, месяц и точное время будильника: ").split()
count_repeat = int(input("Сколько раз повторить: "))
time_repeat = float(input("Через сколько минут повторить: "))
data_difference = ((int(time_alarm[0]) - date_now.day) * 86400) + ((int(time_alarm[1]) - date_now.month) * 30 * 86400) \
                  + ((int(time_alarm[2]) - date_now.hour) * 3600) \
                  + ((int(time_alarm[3]) - date_now.minute) * 60) - date_now.second
print(data_difference)
while True:
    if data_difference > 0:
        print(f"До будильника осталось {data_difference // 60} минут {data_difference % 60} секунд")
        time.sleep(data_difference)
        date_now = datetime.datetime.now()
        data_difference = ((int(time_alarm[0]) - date_now.day) * 86400) + (
                (int(time_alarm[1]) - date_now.month) * 30 * 86400) \
                          + ((int(time_alarm[2]) - date_now.hour) * 3600) \
                          + ((int(time_alarm[3]) - date_now.minute) * 60) - date_now.second
    else:
        if int(time_alarm[0]) == date_now.day and int(time_alarm[1]) == date_now.month \
                and int(time_alarm[2]) == date_now.hour and int(time_alarm[3]) == date_now.minute:
            for i in range(1):
                playsound(sound)
            rerun(time_repeat, count_repeat)
        break
