"""
    Первый тестовый проект
"""
import time


def rerun(x, y):
    for _ in range(x):
        time.sleep(y)
        return (f"Slept for {y // 60} min {y % 60} second")


print(rerun(1, 3))
