import time
from multiprocessing import Process
start = 0
end = 100000

def calculate(start, end):
    total = 0
    for i in range(start,end):
        total += i*i
    pass


if __name__ == "__main__":

    start_time = time.time()

    processes = []

    p = Process(target=calculate, args=(start,end ))
    p.start()
    p.join()

    end_time = time.time()

    print(f"Time: {end_time - start_time:.2f} seconds")