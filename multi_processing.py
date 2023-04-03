import multiprocessing

def calc_square(numbers):
    for n in numbers:
        print('square' + str(n*n))

def calc_cube(numbers):
    for n in numbers:
        print('cube' + str(n*n*n))

if __name__== '__main__':

    arr=[2,5,6,7,8,9,7,8]
    p1= multiprocessing.Process(target= calc_square,args=(arr,))
    p2= multiprocessing.Process(target= calc_cube,args=(arr,))


    p1.start()
    p2.start()

    p1.join()
    p2.join()

print('Done')