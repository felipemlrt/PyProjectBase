 
import os
import sys
import time
 
class Project_base():
    """ This project is meants as a base for projects in python. Mostly aimed at lower level projects for embedded systems, in wich installing many modules is difficult.
    """
  
  def __init__():
   """ Constructor of the class. Used to set required data at runtime.
   """
   pass
  
  def example_method():
   """ Example of method
   """
   try: #usual operation run this
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
  # Code goes here
  # Codigo aqui
  finally:
    os.unlink(pidfile)
    
  except Exception as e:
    return e
  #logger
