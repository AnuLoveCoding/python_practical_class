from threading import Thread
from time import sleep

class A(Thread):
    def run(self):
        for i in range(5):
            print("Anurag")
            sleep(1)
            

class B(Thread):
    def run(self):
        for i in range(5):
            print("Anurag Babu")
            sleep(1)



t1 = A()
t2 = B()


t1.start()
t2.start()

t1.join()
t2.join()


print("Ankit")





