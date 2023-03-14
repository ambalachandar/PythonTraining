import threading
import time

def function1():
    print("Starting function 1...")
    time.sleep(2)  
    print("Function 1 completed.")

def function2():
    print("Starting function 2...")
    time.sleep(3)  
    print("Function 2 completed.")

if __name__ == "__main__":
    t1 = threading.Thread(target=function1)
    t2 = threading.Thread(target=function2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Both threads completed.")
