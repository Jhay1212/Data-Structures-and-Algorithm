import time
import threading

start = time.perf_counter()

def do_something():
    print('sleeping in one second')
    time.sleep(1.5)
    print('done sleeping')
    
threads = []

for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
    
finish_time = time.perf_counter()
print(finish_time - start)