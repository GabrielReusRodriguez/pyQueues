# -*- coding: utf-8 -*-

from EventManager.TypeEvent import TypeEvent
from EventManager.Event import Event
from EventManager.EventManager import EventManager 

class ExitEvent(Event):

    def __init__(self):
        super().__init__(TypeEvent.EXIT_EVENT)

    def run(self):
        EventManager.execute = False
