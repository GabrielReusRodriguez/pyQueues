
# -*- coding: utf-8 -*-

import time

from threading import Thread
from EventManager.Event import Event
from EventManager.ConstantEventManager import ConstantEventManager


class EventManager(Thread):
    
    execute = True

    def __init__(self):
        Thread.__init__(self)
        self._list = list()
    
    def isEmpty(self):
        return len(self._list) == 0
    
    def size(self):
        return len(self._list)

    def append(self,event : Event):
        if event != None:
            self._list.append(event)

    def pop(self):
        if (self.isEmpty() == False) :
            event = self._list.pop(0)
            return event
        else:
            return None
    
    def run(self):
        while( EventManager.execute ):
            evento = self.pop()
            if (evento != None):
                print("Ejecuta")
                evento.run()
            time.sleep(ConstantEventManager.SLEEP_TIME_LOOP)
        self.destroy()

    def destroy(self):
        self._list.clear()