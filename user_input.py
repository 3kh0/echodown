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

import re
from termcolor import colored

def get_ip_address():
  print("Enter IP address:")
  ip = input(colored("> ", "yellow"))

  if not re.match(r"^(\d{1,3}\.){3}\d{1,3}$", ip):
    print(colored("Error: Invalid IP address format at python userInput, promise rejected.", "red"))
    print(colored("Exiting due to error, it was your fault :(", "red"))
    exit("invalid input")
    
  return ip

def get_protocol():
  protocols = {
    1: "TCP", 
    2: "UDP", 
    3: "HTTP"
  }

  print("Select a protocol (TCP, UDP, or HTTP):")
  protocol = input(colored("> ", "yellow"))
    
  if protocol not in ['TCP', 'UDP','HTTP']:
    print(colored("Error: Invalid protocol at python userInput, promise rejected.", "red"))
    print(colored("Exiting due to error, it was your fault :(", "red"))
    exit("invalid input")
    
  return protocol