# -*- coding: utf-8 -*-

from EventManager import TypeEvent

class Event:

    def __init__(self,typeEvent: TypeEvent):
        self._tipoEvento = typeEvent

    def run(self):
        pass
