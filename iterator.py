import time

class FibonacciIterator():

    def __init__(self, max: int):
        self.max = max


    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        self.aux = 0
        return self


    def __next__(self):
        if self.counter == 0 and self.counter < self.max:
            self.counter += 1
            return self.n1
        elif self.counter == 1 and self.counter < self.max:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2

            if self.aux > self.max:
                raise StopIteration
            else:
                self.counter += 1
                self.n1, self.n2 = self.n2, self.aux # esto se llama swap (intercambiar)
                return self.aux


if __name__ == '__main__':
    fibo_in = FibonacciIterator(55)
    fibo_out = FibonacciIterator(39)
    for i in fibo_in:
        print(i)
        time.sleep(0.5)
    for i in fibo_out:
        print(i)
        time.sleep(0.5)
