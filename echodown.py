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


import random
from termcolor import colored
from connection import check_connection
from attack import start_attack
from user_input import get_ip_address, get_protocol, get_thread_num
from pick import pick # https://github.com/wong2/pick
from time import sleep
def main():
  print()
  print(colored("Starting Echo Down, please hold on!", "red"))
  print(colored("I am sure you are using this for legal purposes - Echo", "red"))
  print()

  check_connection()

  print(colored('''
                
       ███████╗░█████╗░██╗░░██╗░█████╗░  ██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗
       ██╔════╝██╔══██╗██║░░██║██╔══██╗  ██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║
       █████╗░░██║░░╚═╝███████║██║░░██║  ██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║
       ██╔══╝░░██║░░██╗██╔══██║██║░░██║  ██║░░██║██║░░██║░░████╔═████║░██║╚████║
       ███████╗╚█████╔╝██║░░██║╚█████╔╝  ██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║
       ╚══════╝░╚════╝░╚═╝░░╚═╝░╚════╝░  ╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝
       
''', 'red'))
  print(colored("                      The most powerful DDoS tool out there","red",attrs=["bold"],))
  print()
  menu_selections = [
    'Start',
    'Credits',
    'Exit'
  ]
  sleep(2)
  menu_selection = pick(menu_selections, 'Pick an option...', '> ')[0]
  match menu_selection:
    case 'Start':
      ip = get_ip_address()
      protocol = get_protocol()
      threads = get_thread_num()
      print(colored("Launched with " + str(threads) + " threads.", "cyan"))
      print()
      start_attack(ip, protocol, threads)
    case 'Credits':
      print(colored('                        ECHODOWN', attrs=['bold']))
      print(colored('''
            Star us on github!
            https://github.com/3kh0/echodown
            
            Developers
            @3kh0
            @aeiea
            @RuralAnemone
            ''', 'green'))
    case 'Exit':
      exit(0)
  

if __name__ == "__main__":
  main()
