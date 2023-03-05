# -*- coding: utf-8 -*-

from EventManager.TypeEvent import TypeEvent
from EventManager.Event import Event

class DummyEvent(Event):

    def __init__(self):
        super().__init__(TypeEvent.DUMMY_EVENT)

    def run(self):
        print("Evento Dummy")
