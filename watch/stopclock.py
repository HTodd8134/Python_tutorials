import time

def counter(sec):
    mins = sec//60
    hours = mins//60
    print("time lapsed = {0}:{1}:{2}".format(int(hours),int(mins),int(sec)))

input("press enter to start")
start_time = time.time()

input("press enter to stop")
end_time = time.time()

time_elapsed = end_time - start_time
counter(time_elapsed)