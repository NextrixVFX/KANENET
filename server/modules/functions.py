from os import system, name
from socket import socket
from json import loads

class config:
  def __init__(self) -> None:
    self.database = loads(open("./database.json", 'r+').read())
    self.blacklist = loads(open("./blacklist.json", 'r+').read())
    self.config = loads(open("./config.json", 'r+').read())

class data:
  def __init__(self) -> None:
    pass

  def recieve(self, server: socket) -> str:
    waiting: int = 0
    while True:
      recieved: bytes = server.recv(1024).decode("utf-8")
      if not recieved:
        if waiting < 20: # not borrowed from verm bc lazy
          waiting += 1
        else:
          break
      return recieved
    
  def send(self, server: socket, data: str) -> None:
    server.send(data.encode("utf-8"))


# console clear text: \033[2J\ or \033[H

CLEAR: str = "\033[2J \033[H"
 
# clear console?
def clear() -> None:
  system('cls' if name == 'nt' else 'clear')

def splash(data: list[str, str]) -> str:
  # data -> [USERNAME, RANK]
  screen: str = f"""{CLEAR}
  KANENET v0.1.2 - nextrixvfx
  Welcome: {data[0]}
  Rank: {data[1]}
  \nType: help"""
  return screen

def helpText() -> str:
  help: str = f"""{CLEAR}
  Attacks:
  \tudp - Performs UDP Attack w/ float64 data [ 3100 Max Size ]
  \ttcp - Performs TCP Attack w/ float64 data (Target's port has to be OPEN!) [ 5000 Max Size? Maybe? ]
  \tpost - Performs POST Attack w/ custom data (Used for backends)

  Etc:
  \tping - Responds Pong!
  \thelp - take a guess...
"""
  return help

if __name__ == "__main__":
  exit()