# -*- coding: utf-8 -*-

import logging
from LogManager.LogLevels import LogLevels

class LoggerAdapter:

    #def __init__(self, level: LogLevels = LogLevels.INFO):
    def __init__(self, level: LogLevels = LogLevels.ERROR):
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=level.value, datefmt="%H:%M:%S")
    
    def info(self, msg):
        logging.info(msg)
    
    def debug(self, msg):
        logging.debug(msg)

    def error(self,msg):
        logging.error(msg)
    
    def warning(self,msg):
        logging.warning(msg)
    
    def critical(self,msg):
        logging.critical(msg)