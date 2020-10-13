"""
    Первый тестовый проект
"""
import time


def rerun(count, second):
    for _ in range(count):
        time.sleep(second)
        return (f"Slept for {second // 60} "
                f"min {second % 60} second")


print(rerun(1, 3))
