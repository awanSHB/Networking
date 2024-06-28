import threading
def print_numbers():
    for i in range(1, 6):
        print(f"Thread: {threading.current_thread().name}, Number: {i}")
threads = []
for i in range(3):
    thread = threading.Thread(target=print_numbers)
    threads.append(thread)
    thread.start()
## Joining Threads:
## Demonstrate the use of the join() method to ensure that the main program waits for all threads to complete before proceeding
for thread in threads:
    thread.join()
print("All threads have completed.")
## Implement a shared variable and use locks to synchronize access to it.
shared_variable = 0
lock = threading.Lock()
def increment_shared_variable():
    global shared_variable
    for _ in range(1000000):
        lock.acquire()
        shared_variable += 1
        lock.release()
threads = []
for i in range(5):
    thread = threading.Thread(target=increment_shared_variable)
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
print("Final value of shared variable:", shared_variable)
