import datetime
import time

"""
    функция промежуток между звонками с двумя повторениями

    попытка все обернуть в класс
"""
class Povtor():
    def rerun(self,x, y):
        self.count = x
        for _ in range(self.count):
            time.sleep(y)
            return (f"Slept for {y // 60} min {y % 60} second")


print(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
