#
# ███████╗░█████╗░██╗░░██╗░█████╗░  ██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗
# ██╔════╝██╔══██╗██║░░██║██╔══██╗  ██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║
# █████╗░░██║░░╚═╝███████║██║░░██║  ██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║
# ██╔══╝░░██║░░██╗██╔══██║██║░░██║  ██║░░██║██║░░██║░░████╔═████║░██║╚████║
# ███████╗╚█████╔╝██║░░██║╚█████╔╝  ██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║
# ╚══════╝░╚════╝░╚═╝░░╚═╝░╚════╝░  ╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝
#
#                   https://github.com/3kh0/echodown

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
  print("Select a protocol (TCP, UDP, or HTTP):")
  protocol = input(colored("> ", "yellow"))
    
  if protocol not in ['TCP', 'UDP','HTTP']:
    print(colored("Error: Invalid protocol at python userInput, promise rejected.", "red"))
    print(colored("Exiting due to error, it was your fault :(", "red"))
    exit("invalid input")
    
  return protocol
def get_thread_num():
  print("Enter number of threads(default 16): ")

  threads = input(colored("> ", "yellow"))
  if threads == None:
    threads = 16
  else:
    try:
      threads = int(threads)
    except:
      print(colored("Error: Non-integer value at python userInput, failed to start threads.", "red"))
      print(colored("Exiting due to error, it was your fault :(", "red"))
      exit("invalid input")
  return threads
