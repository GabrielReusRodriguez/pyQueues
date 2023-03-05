#!/bin/env python3

# -*- coding: utf-8 -*-

import logging
import threading
import time
from ReadBuffer import *

print  ("hola mundo!\n")


def thread_fn(name):
    logging.info("Thread %s: start",name)
    time.sleep(2)
    logging.info("Thread %s: finishing",name)



if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")
    buffer = ""
    threads = list()
    buffer1 = Buffer()
    buffer2 = Buffer()

    thread1 = threading.Thread(target=buffer1.bufferRead, args=())
    threads.append(thread1)
    thread1.start()

    thread2 = threading.Thread(target=buffer2.bufferRead, args=())
    threads.append(thread2)
    thread2.start()

#    for index in range(3):
#        logging.info("Main:Create and start thread %d",index)
#        x = threading.Thread(target=thread_fn, args=(index,))
#        threads.append(x)
#        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main   :before joining thread %d",index)
        thread.join()
        logging.info("Main    : thread %d done",index)