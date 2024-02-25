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

# Here is actual code to spam ping something,
# this is for a legal reason correct??

import subprocess
import time

# Replace "192.168.1.1" with the IP address you want to ping
ip_address = "192.168.1.1"

while True:
  ping_output = subprocess.run(['ping', '-c', '1', ip_address], stdout=subprocess.PIPE)

  ping_time = None
  for line in ping_output.stdout.decode('utf-8').split('\n'):
    if 'time=' in line:
      ping_time = int(line.split('time=')[1].split()[0])
      break

  if ping_time is not None:
    print(f"Ping to {ip_address} took {ping_time} ms")
  else:
    print(f"Ping to {ip_address} failed")
