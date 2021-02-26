class connector():
 """ Simple connector application. Mainly focused in making the code cleaner and easier to read.
 """
 url = "127.0.0.1"
 password = "admin"
 login = "admin"
 database = "test"
 
 def __init__(self, url, login, password, database):
  try:
   self.url = url
   self.password = password
   self.login = login
   self.database = database
  except Exeption as e:
   print(e)
   
 def connect()
 def disconnect()
 def select()
 def insert()
 def delete()
