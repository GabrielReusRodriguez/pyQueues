
# -*- coding: utf-8 -*-
import threading

class Buffer:

    #static
    buffer = ""    

    def __init__(self):
        self._lock = threading.Lock()
        #self._buffer =  buffer
        
    
    def bufferRead(self):

        char = "a"

        with self._lock:
            #self._buffer = self._buffer + char
            ReadBuffer.buffer = ReadBuffer.buffer + char 

        #print("buffer : %s ",self._buffer)
        print("buffer : ",ReadBuffer.buffer)

