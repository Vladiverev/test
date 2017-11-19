#iterator

class MyOwnIteration:
    def __iter__(self):
        return self
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration

itr = MyOwnIteration(3)
for i in itr:
    print(i)
