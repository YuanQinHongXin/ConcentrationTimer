import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

def start_pomodoro():
    print("Pomodoro Timer - 25 minutes")
    countdown(25)

    print("Take a short break - 5 minutes")
    countdown(5)

    print("Pomodoro Timer - 25 minutes")
    countdown(25)

    print("Take a short break - 5 minutes")
    countdown(5)

    print("Pomodoro Timer - 25 minutes")
    countdown(25)

    print("Take a long break - 15 minutes")
    countdown(15)

start_pomodoro()
