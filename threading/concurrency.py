from concurrent import futures
import time

start = time.perf_counter()
def hello(sec):
    print('h')
    time.sleep(sec)
    return 'done with this {}'.format(sec)

with futures.ThreadPoolExecutor() as ex:
    secs = [5, 4, 3, 2, 1]
    results = ex.map(hello, secs)
    for res in results:
        print(res)
end = time.perf_counter()
print(end - start)