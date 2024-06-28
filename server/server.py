from modules.functions import splash, config, data
from modules.commands import Commands
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_KEEPALIVE
from time import sleep

class server:
  def __init__(self) -> None:
    self.commands: Commands = Commands()
    self.data: data = data()
    self.config: config = config()
    self.ip = self.config.config["ip"]
    self.port = self.config.config["port"]

    self.s: socket = socket(AF_INET, SOCK_STREAM)
    self.s.setsockopt(SOL_SOCKET, SO_KEEPALIVE, 1) # rad

    self.s.bind((self.ip, self.port))
    self.s.listen(int(self.config.config["max-connections"]))
    print(f"Listening! : {self.ip}:{self.port}\n")
    
  def handleOnLogin(self, server: socket, data: list[str, str]) -> None:
    while True:
      try:
        try:
          self.data.send(server, splash(data))
          sleep(0.5)
          op: str = self.data.recieve(server)
          match op:
            case "UDP":
              self.commands.udp(server, data)
              sleep(0.5)
            case "PING":
              self.commands.ping(server, data)
              sleep(0.5)
            case "HELP":
              self.commands.help(server, data)
              sleep(0.5)
            case _:
              print(f"{data[0]}: {op} -> Not Valid")
        except Exception as e:
          print(f"{data[0]}: Disconnected...\nERR:\t{e}")
          break
      except KeyboardInterrupt:
        exit() 
    
  def main(self) -> None:
    self.conn, self.addr = self.s.accept()
    with self.conn as c:
      blacklisted = False
      for x in self.config.blacklist["user-ip"]:
        if str(self.addr).__contains__(x):
          print(f"Blacklisted user: {self.addr} tried connecting!")
          blacklisted = True
          break

      if not blacklisted:
        print(f"Incoming Connection: {self.addr}")
        self.username = str(self.data.recieve(c))
        sleep(0.5)
        self.password = str(self.data.recieve(c))
        print(f"Incoming {self.addr} used: {self.username}:{self.password}")
        try:
          self.GetUser = self.config.database[self.username]
          self.GetRank = self.config.database[self.username]["rank"]
        except:
          self.data.send(c, "\033[H\nUser/Pass Not Valid!")

        try:
          if self.GetUser["password"] == self.password:
            self.data.send(c, "Success")
            print(f"{self.username} Connected -- Rank: {self.GetRank}")
            self.handleOnLogin(c, [self.username, self.GetRank])
          else:
            self.data.send(c, "\033[H\nUser/Pass Not Valid!")
        except Exception as e:
          self.data.send(c, f"\033[H\nSomf went wrong cuh: {e}")


if __name__ == "__main__":
  Server: server = server()
  while True:
    Server.main()
else:
  exit()



