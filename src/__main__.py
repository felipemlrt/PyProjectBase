 
import os
import sys
import time
 
class Project_base():
    """ A base for projects in python. Mostly aimed at lower level projects for embedded systems.
    """
  
  def __init__():
   """ Constructor of the class.
   """
   pass
  
  def example_method():
   """ Example of method
   """
   pass

if __name__ == "__main__":
  # Code that will only run if this file is run as the initial point.
  pid = str(os.getpid())
  pidfile = "/tmp/file_lock.pid"

  if os.path.isfile(pidfile):
      print ("%s already exists, exiting") % pidfile
      sys.exit()
  file(pidfile, 'w').write(pid)
  try:
  # Do some actual work here
  finally:
    os.unlink(pidfile)
    
  except Exception as e:
    return e
  #logger
  #exeption handling
