# -*- coding: utf-8 -*-

#import TypeEvent
from EventManager.TypeEvent import TypeEvent
from EventManager.Events.DummyEvent import DummyEvent
from EventManager.Events.ExitEvent import ExitEvent

class EventFactory():

    def buildEvent(tipoEvento : TypeEvent ):
        return {
            TypeEvent.DUMMY_EVENT: lambda: EventFactory.__buildDummyEvent(),
            TypeEvent.EXIT_EVENT: lambda : EventFactory.__buildExitEvent()

        }.get(tipoEvento,lambda: None )()
    
    def __buildDummyEvent():
        return DummyEvent()
    
    def __buildExitEvent():
        return ExitEvent()


#        match tipoEvento:
#
#            case TypeEvent.DUMMY_EVENT:
#                evento = DummyEvent()
#
#            case _:
#                return None
#
#        #pass


#def opera2(operador, a, b):
#    return {
#        'suma': lambda: a + b,
#        'resta': lambda: a - b,
#        'multiplica': lambda: a * b,
#        'divide': lambda: a / b
#    }.get(operador, lambda: None)