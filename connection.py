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
from halo import Halo

waitTime = 0.5

def check_connection():
  with Halo(text=colored("Checking Connection", "yellow"), spinner="dots") as h1:
    time.sleep(waitTime)
    h1.succeed(colored(" Check Connection", "green"))

  with Halo(text=colored("Importing Packages", "yellow"), spinner="dots") as h2:
    time.sleep(waitTime)
    h2.succeed(colored(" Import Packages", "green"))

  with Halo(text=colored("Downloading Scripts", "yellow"), spinner="dots") as h3:
    time.sleep(waitTime)
    h3.succeed(colored(" Download Scripts", "green"))

  with Halo(text=colored("Fetching Files", "yellow"), spinner="dots") as h4:
    time.sleep(waitTime)
    h4.succeed(colored(" Fetch Files", "green"))

  with Halo(text=colored("Compiling", "yellow"), spinner="dots") as h5:
    time.sleep(waitTime)
    h5.succeed(colored(" Compile", "green"))

  with Halo(text=colored("Detecting Hardware", "yellow"), spinner="dots") as h6:
    time.sleep(waitTime)
    h6.succeed(colored(" Detect Hardware", "green"))

  with Halo(text=colored("Starting Proxy", "yellow"), spinner="dots") as h7:
    time.sleep(waitTime)
    h7.succeed(colored(" Start Proxy", "green"))

  with Halo(text=colored("Starting Hosted Threads", "yellow"), spinner="dots") as h8:
    time.sleep(waitTime)
    h8.succeed(colored(" Start Hosted Threads", "green"))

  with Halo(text=colored("Requesting RAM from System", "yellow"), spinner="dots") as h9:
    time.sleep(waitTime)
    h9.succeed(colored(" Request RAM", "green"))

  with Halo(text=colored("Booting", "yellow"), spinner="dots") as h10:
    time.sleep(waitTime)
    h10.succeed(colored(" Boot", "green"))