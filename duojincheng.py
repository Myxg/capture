import time
from multiprocessing import Process


def run(name):
    print(name+'1')
    time.sleep(5)
    print(name+'2')


p1 = Process(target=run, args=('a',))
p2 = Process(target=run, args=('b',))
p3 = Process(target=run, args=('c',))
p4 = Process(target=run, args=('d',))

if __name__ == '__main__':
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    #
    # p1.join()
    # p2.join()
    # p3.join()
    # p4.join()

    print('主线程')

