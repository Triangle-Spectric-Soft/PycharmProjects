class QueueError(Exception):
    pass


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def put(self, item):
        self.items.append(item)

    def get(self):
        if self.is_empty():
            raise QueueError("Queue is empty")
        return self.items.pop(0)


class SuperQueue(Queue):
    def isempty(self):
        return self.is_empty()


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
