from eventlet.green import threading
import time


def my_counter():
    i = 0
    for _ in range(40000000):
        i += 1

    return True


def main():
    thread_array = {}
    start_time = time.time()
    for _ in range(2):
        t = threading.Thread(target=my_counter)
        t.start()
        t.join()
    end_time = time.time()

    print "total time: {}".format(end_time - start_time)


main()