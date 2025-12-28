from collections import deque

custom_queue = deque(maxlen=5)
custom_queue.append(12)
custom_queue.append(1)
custom_queue.append(1)
custom_queue.append(1)

print(custom_queue)
print(custom_queue)