 
import os #this code is meant for linux as it is the more easily used embedded os and very common 
import sys
import time
import logging
 
class project_base():
    """ This project is meants as a base for projects in python. Mostly aimed at lower level projects for embedded systems, in wich installing many modules is difficult.
    """
  log = None
  
  def __init__(self):
   """ Constructor of the class. Used to set required data at runtime.
   """
   self.log = logging.getLogger(__name__)
   pass
  
  def example_method(self):
   """ Example of method
   """
   try:
     #first this will run
     pass 
   except Exception as e: #in case any exceptions are raised this will run
     print(e) #at least log and/or print
   else: #if no exceptions are raised this will run
    pass
   finally: #this will run regardless of exceptions or not
     pass #for instance closing a connection with a database should be done regardless of the operations being done or not.
  
  def find_path():
   try:
    pass
   except Exception as e:
    print("Could not locate file path")
    print(e)
   
if __name__ == "__main__":
 try:
  # Code that only lets the program run if it is not already running.
  # Codigo que verifica se o programa ja esta em execucao.
  pid = str(os.getpid())
  pidfile = "/tmp/file_lock.pid"
  if os.path.isfile(pidfile):
      #recovering for unexpected shutdowns this file may need to be cleared
      print ("One istance is already open!")
      sys.exit()
  file(pidfile, 'w').write(pid)
  print("Starting run, EXAMPLE V.01")
  # Code goes here
  # Codigo aqui
  finally:
    os.unlink(pidfile)
    
  except Exception as e:
    return e
  #logger
