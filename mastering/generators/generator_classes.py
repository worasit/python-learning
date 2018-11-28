import sys


class Count(object):
    def __init__(self, start=1, stop=1000, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        # Need to raise `StopIteration()` for avoiding inifinite counting
        if self.start > self.stop:
            raise StopIteration()
        self.start += self.step
        return self.start


for i in Count(0, 10, 1):
    print(i)
