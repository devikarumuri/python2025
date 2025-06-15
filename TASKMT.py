#multithreading
import time
import threading
def square(numbers):
    print("square number")
    for i in numbers:
        time.sleep(0.5)
        print(f"square:{i*i}")

def cube(numbers):
    print("cube number:")
    for i in numbers:
        time.sleep(0.5)
        print(f"cube:{i*i*i}")

initial_time=time.time()
l=[1,2,3,4,5,6,7,8,9,10] 


thread1=threading.Thread(target=square,args=(l,))
thread2=threading.Thread(target=cube,args=(l,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()