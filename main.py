"""
    Первый тестовый проект
"""
import time
from playsound import playsound


def rerun(time_repeat, count):
    for _ in range(count):
        time.sleep(time_repeat * 60)
        return (f"Slept for {int(time_repeat)} "
                f"min {int((time_repeat * 60) % 60)} second")


# count = int(input("Сколько раз повторить: "))
# time_repeat = float(input("Через сколько минут повторить: "))
#
# print(rerun(time_repeat, count))
sound = "C:\\Users\\Stuffing\\PycharmProjects\\Firstproject\\miniproject\\mp3\\night-owl.mp3"
playsound(sound)
