import  time


def rerun(repeat, count):
    for _ in range(count):
        time.sleep(repeat * 60)
        for _ in range(5):
            return playsound(sound)