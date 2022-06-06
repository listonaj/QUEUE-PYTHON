# Jean-Marc Romain
# 06-05-2022
# implementation of a queue using list in python with no specifiation of size

class Queue:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items ==[] :
            return True
        else:
            return False
    
    def enqueue(self, value):
        self.items.append(value)
        return f"the element {value} has been added to the Queue"

    def dequeue(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            return self.linkedList.head
    
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None