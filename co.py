import asyncio
import threading
import time
from multiprocessing import Process

start = time.time()

files = [
    "lecture1.pdf",
    "lecture2.pdf",
    "assignment.zip",
    "slides.pptx",
    "python_notes.pdf"
]
def download_file(file_name):
    print(f"downloading {file_name}")
    time.sleep(2)
    print(f"downloaded {file_name}")

#Is this task CPU-bound or I/O-bound? I/O bound
#Why is threading appropriate? threat is for I/O bound
#Would multiprocessing improve performance here? no

s = 0
e = 20000000
def calculate(s,e):
    total = 0
    for i in range(s,e):
        total += i*i
    return total
async def fetch(user_id):
    await asyncio.sleep(2)
    return {"id": user_id, "status": "OK"}
async def main():
    start = time.time()
    result1 = await fetch(1)
    result2 = await fetch(2)
    result3 = await fetch(3)
    end = time.time()
    print(result1)
    print(result2)
    print(result3)
    print(f"{end - start} seconds")

    start = time.time()
    results = await asyncio.gather(fetch(1),fetch(2),fetch(3))
    print(results)
    end = time.time()
    print(f"{end - start} seconds")

if __name__ == "__main__":
    start = time.time()
    threads = []
    for file in files:
        t = threading.Thread(target=download_file, args=(file,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    end = time.time()
    print("all downloaded")
    print(f"{end - start} seconds")


    start = time.time()
    ranges = [(0,5000000),(5000000,10000000),(10000000,15000000),(15000000,20000000)]
    processes = []
    for s, e in ranges:
        p = Process(target=calculate,args=(s,e))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

    end = time.time()

    print(f"{end - start} seconds")
    asyncio.run(main())
#Why not use threads? because this is CPU bound
#What role does the GIL play? make thread not useful for cpu bound
#Why does each process have its own memory? to prevents interference between processes
#Question 1
#A web crawler needs to download 10,000 web pages. Which would you choose?
#ANS AsyncIO because it's suit for massive I/O bound

#Question 2
#An AI model needs to train on 50 million images. Which model? Explain.
#ANS Multiprocessing because training Ai is cpu task
#Question 3
#An image editor applies filters to 2000 photos. Which model? Explain.

#Question 4
#A chat server handles 50,000 connected users. Which model? Explain.

#Question 5
#Explain the difference between concurrency parallelism using your own words.

#Question 6
#What is the Event Loop?

#Question 7
#Why does Python have a GIL?

#Question 8
#Why don't processes share variables?
