class example_queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) == 0:
            return 'there is nothing in the queue'
        return self.queue.pop(0)

    def print_queue(self):
        return self.queue

queue = example_queue()
print('test case 1')
print()
print(queue.dequeue())
print()
print('test case 2')
print()
queue.enqueue(1)
queue.enqueue(4)
queue.enqueue(3)
queue.enqueue(10)
print(queue.dequeue())
print(queue.dequeue())
print(queue.print_queue())

        