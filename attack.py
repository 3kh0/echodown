#
# ███████╗░█████╗░██╗░░██╗░█████╗░  ██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗
# ██╔════╝██╔══██╗██║░░██║██╔══██╗  ██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║
# █████╗░░██║░░╚═╝███████║██║░░██║  ██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║
# ██╔══╝░░██║░░██╗██╔══██║██║░░██║  ██║░░██║██║░░██║░░████╔═████║░██║╚████║
# ███████╗╚█████╔╝██║░░██║╚█████╔╝  ██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║
# ╚══════╝░╚════╝░╚═╝░░╚═╝░╚════╝░  ╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝
#
#                   https://github.com/3kh0/echodown
#

import time
import random
from termcolor import colored

def start_attack(ip, protocol, threads):
  print(colored("Target set to " + ip + " using " + protocol + ".", "magenta",))
  print(colored("Starting attack with " + str(threads) + " threads, use CTRL+C to stop at any time", "magenta",))
  print(colored("You can use https://iplocation.io/ping/" + ip + " to check the webserver ping.","magenta",))
  print()
  while True:
    mbSec = round(random.uniform(10, 40), 1)
    hitRate = round(random.uniform(95, 100), 2)
    curThread = random.randint(1, threads)
    if random.randint(1, 1000) < 10:
      print(colored("Thread {}: Packet failed to send, trying again.".format(curThread),"red",))
    else:
      print(colored("Thread {}: {}MB sent in the last second to target with a {}% Hitrate on requests.".format(curThread, mbSec, hitRate),"green",))
    time.sleep(1)
