import time

def countdown(timer):
    while timer:
        min, sec = divmod(timer, 60)
        timerformat = '{:02d}:{:02d}'.format(min, sec)
        print(timerformat, end='\r')
        time.sleep(1)
        timer -= 1


timer = input("Enter the start timer: ")
countdown(int(timer))