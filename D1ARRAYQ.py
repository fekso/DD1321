from array import array
#li = [7,1,12,2,8,3,11,4,9,5,13,6,10]

class ArrayQ:
    def __init__(self):
        self.__queue = array('i')
    def dequeue(self):
        return self.__queue.pop(0)
    def enqueue(self, x):
        self.__queue.append(x)
    def isEmpty(self):
        if not self.__queue:        
            return True
        else:
            return False
