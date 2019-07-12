import multiprocessing
import threading
import time


output = multiprocessing.cpu_count()

print(output)

#print_lock = threading.Lock()

def Func1():
    #with print_lock:
    print("h" + "1")

def Func2():
    #with print_lock:
    print("c" + "2")

def Func3():
    #with print_lock:
    print("s" + "3")

def Func4():
    #with print_lock:
    print("f" + "4")

def Func5():
    #with print_lock:
    print("b" + "5")

def Func6():
    #with print_lock:
    print("n" + "6")

def Func7():
    #with print_lock:
    print("m" + "7")

def Func8():
    #with print_lock:
    print("k" + "8")

def Func9():
    #with print_lock:
    print("y" + "9")

t1 = threading.Thread(target=Func1)
t2 = threading.Thread(target=Func2)
t3 = threading.Thread(target=Func3)
t4 = threading.Thread(target=Func4)
t5 = threading.Thread(target=Func5)
t6 = threading.Thread(target=Func6)
t7 = threading.Thread(target=Func7)
t8 = threading.Thread(target=Func8)
t9 = threading.Thread(target=Func9)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()