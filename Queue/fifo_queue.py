import queue as q
from multiprocessing import Queue

cQueue = Queue

custom_queue = q.Queue(maxsize=4)

custom_queue.put(4)
custom_queue.put("jhay")
custom_queue.put("zeef")

print(custom_queue.qsize())
print(custom_queue.is_shutdown)
print(custom_queue.all_tasks_done())
