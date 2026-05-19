class fibonacci:
    def __init__(self, n):
        self.n = n
        self.i = 0
        self.j = 1
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        value = self.i
        self.i, self.j = self.j, self.i + self.j
        self.count +=1
        return value
x = fibonacci(10)
for num in x:
    print(num)
