from abc import ABC, abstractmethod

class BaseMinStack(object):
    """docstring for BaseMinStack"""
    def __init__(self):
        self.stack = []
        pass

    @abstractmethod
    def push(self, x: int) -> None:
        pass

    @abstractmethod
    def pop(self) -> None:
        pass

    @abstractmethod
    def top(self) -> int:
        pass

    @abstractmethod
    def getMin(self) -> int:
        pass

class MinStack(BaseMinStack):
    """
    This is the most basic form possible using built-in python.
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        super(MinStack, self).__init__()
        

    def push(self, x: int) -> None:
    	self.stack.append(x)
        

    def pop(self) -> None:
    	self.stack.pop()
        

    def top(self) -> int:
    	return self.stack[-1]
        

    def getMin(self) -> int:
    	return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
x = 10
obj = MinStack()
obj.push(x)
param_3 = obj.top()
obj.pop()
obj.push(x)
param_4 = obj.getMin()