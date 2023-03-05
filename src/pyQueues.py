#!/bin/env python3

# -*- coding: utf-8 -*-

from LogManager.LoggerAdapter import LoggerAdapter
from LogManager.LogLevels import LogLevels
from EventManager.EventManager import EventManager
from EventManager.EventFactory import EventFactory
from EventManager.TypeEvent import TypeEvent

#def thread_fn(name):
#    logging.info("Thread %s: start",name)
#    time.sleep(2)
#    logging.info("Thread %s: finishing",name)


if __name__ == "__main__":

    logger = LoggerAdapter(LogLevels.INFO)
    index = 2
    logger.info("Hola " + str(index) + " mundo!")
    eventManager = EventManager()
    eventManager.start()
    while EventManager.execute ==  True:
        entrada = input("Entra el comando: ")
        evento = None
        if entrada == "d":
            evento = EventFactory.buildEvent(TypeEvent.DUMMY_EVENT)
        elif entrada == "x":
            evento = EventFactory.buildEvent(TypeEvent.EXIT_EVENT)
        eventManager.append(evento)
    print("Final")



    #print("Ejecucion " + str(EventManager.execute) )
    #print("IsEmpty: "+str(eventManager.isEmpty()))
    #evento = EventFactory.buildEvent(TypeEvent.DUMMY_EVENT)
    #print("Evento 2 : "+str(evento._tipoEvento))
    #eventManager.append(evento)
    #print("IsEmpty: "+str(eventManager.isEmpty()))

    #evento2 = EventFactory.buildEvent(TypeEvent.DUMMY_EVENT)
    #print("Evento 2 : "+str(evento2._tipoEvento))
    #eventManager.append(evento2)
    #print("Pre-Ejecuta")
    #eventManager.executeLoop()
#    print(LogLevels.INFO)