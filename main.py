import telnetlib

telnet = None
HOST = "localhost"
DEFAULT_PORT = "5554"

def open_connection():
  global telnet

  if telnet == None:
    telnet = telnetlib.Telnet(HOST, DEFAULT_PORT)
  else:
    telnet.open(HOST, DEFAULT_PORT)

def close_connection():
  global telnet
  
  if telnet != None:
    telnet.close()

def main():
  print " "
  print " "
  print "***********************************************"
  print "* GPS Feeder - Simple Android Emulator Feeder *"
  print "***********************************************"
  print " "
  print " "
  # TODO: Load the GPS Coordinates file

if __name__ == '__main__':
  main()
  open_connection()
  close_connection()