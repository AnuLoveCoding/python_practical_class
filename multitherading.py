from threading import Thread
from time import sleep

class A(Thread):
    def name(self):
        for i in range(5):
            print("Anurag")
            sleep(2)
            

class B(Thread):
    def name1(self):
        for i in range(5):
            print("Anurag Babu")
            sleep(4)



t1 = A()
t2 = B()


t1.start()
t2.start()





