#Jean-Marc Romain
#06-05-2022
# I have tested the implementation of the Queue using list with no limit of size 
# the method are located in the file 'QueuePyList.py'

from QueuePyList import *

customqueue = Queue()

print('Tetsting to see if the queue is empty')
print(customqueue.isEmpty())


print("\nAdding some elements to the queue")
customqueue.enqueue(1) 
customqueue.enqueue(3) 
customqueue.enqueue(6) 
customqueue.enqueue(9) 

print("\nTetsing again to see if the queue is empty")
print(customqueue.isEmpty())

print("\nPrinting the Queue list created")
print(customqueue)

print("\ntesting the dequeue method")
elemremoved = customqueue.dequeue()
print(f"I remove the first element of the list {elemremoved}")
print(customqueue)

print("\nTesting the peek method")
print(customqueue.peek())

print("\n Testing the delete method")
customqueue.delete()

