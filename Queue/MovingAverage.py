"""
#: 346
Title: Moving Average from Data Stream
Description:
------
Given a stream of integers and a window size, calculate the moving average of
all integers in the sliding window.

For example,
```
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
```
------
Time: O(1)
Space: O(k) # size of queue
Difficulty: Easy
"""

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        from collections import deque
        self.lst = deque(maxlen=size)


    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.lst.append(val)
        return float(sum(self.lst))/len(self.lst)


if __name__ == '__main__':
    obj = MovingAverage(3)
    inp_list = [1, 10, 3, 5]
    for i in inp_list:
        print obj.next(i)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
