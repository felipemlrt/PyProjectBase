import logging
import os
import sys

def class logger():
 """ Simple logger application. Copy to all modules.
 """
 logger = None

 def __init__(self):
  try:
   logfile = os.path.dirname(os.path.abspath(__file__)) + "/logs/" + __name__ + ".log" 
   #gets current directory and add /logs/ to it, if the directory /logs does not exists it will give an error.
   log_format = ('[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s')
   logging.basicConfig(level=logging.DEBUG,format=log_format,handlers=[logging.FileHandler(logfile),logging.StreamHandler(sys.stdout)])
   self.logger = logging.getLogger(__name__)
   #this makes so that the logger of each module will have the same name as that of the module
   self.logger.debug("Objeto de verificacao criado")
  except Exception as e:
   msg = "Erro: init: " + e
   self.logger.debug(msg)
   
 def example(self):
  try:
   msg = "Whatever you want to go to the log."
   self.logger.debug(msg)
