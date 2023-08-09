import time

def counter(sec):
    secs = int(sec)
    mins = sec//60
    hours = mins//60
    print(f"time lapsed = {hours}:{mins}:{secs}")

input("press enter to start")
start_time = time.time()

input("press enter to stop")
end_time = time.time()

time_elapsed = end_time - start_time
counter(time_elapsed)