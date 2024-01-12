import time
import winsound

WORK_MIN = 25
SHORT_BREAK_MIN = 5 
LONG_BREAK_MIN = 15
WORK_SESSIONS_BEFORE_LONG_BREAK = 3

session_count = 0
while True: 
    session_count += 1
    session_complete = work_timer(WORK_MIN)
    if session_complete:
        if session_count % WORK_SESSIONS_BEFORE_LONG_BREAK == 0:
            session_complete = break_timer(LONG_BREAK_MIN)
        else:
            session_complete = break_timer(SHORT_BREAK_MIN)

def work_timer(work_minutes):
    print('Work Time (' + str(work_minutes) + ' minutes):')
    return countdown(work_minutes * 60)
  
def break_timer(break_minutes):  
    print('Break Time (' + str(break_minutes) + ' minutes):')
    return countdown(break_minutes * 60)

def countdown(seconds):
    while seconds > 0:
        print_remaining(seconds)
        time.sleep(1)
        seconds -= 1
    beep()
    return True

def print_remaining(seconds):
    print(seconds, 'seconds remaining', end="\r")
  
def beep():
    freq = 800
    duration = 1000
    winsound.Beep(freq, duration)
