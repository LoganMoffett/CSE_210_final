import collections

class customer_queue:
    def __init__(self):
        """
        Initilizes a queue full of customers
        """
        queue = collections.deque()

    def enqueue(self, name):
        """
        This will add a customer to the queue
        """
        pass

    def dequeue(self):
        """
        This will return the next customer so that we can assist them
        """
        pass

    def curr_queue(self):
        """
        This will return the entire queue so we know who is in line.
        """
        pass


#Test Casses
queue = customer_queue()
print("test Case 1")
# we are going to test if we can dequeue from an empty queue
print(queue.dequeue()) 

print()
print("test case 2")
#We are going to test to see if we can enqueue individuals
queue.enqueue("bob")
queue.enqueue("Joe")
queue.enqueue("frank")
print(queue.dequeue())

print()
print('Test Case 3')
# We are going to try a couple of enqueue, dequeue, and curr_queue
queue.enqueue("jill")
print(queue.dequeue())
print(queue.dequeue())
queue.enqueue("test")
print(queue.curr_queue())

