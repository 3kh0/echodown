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
import time
import re
import requests
from termcolor import colored
from halo import Halo

def get_location(ip):
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    if response.status_code == 200:
        data = response.json()
        city = data.get('city')
        country = data.get('country')
        region = data.get('region')
        timezone = data.get('timezone')
        return city, country, region, timezone
    else:
        print("Failed to fetch location data.")
        return None, None, None, None

def start_attack(ip, protocol, city, country, region, timezone):
    if city:
        print(colored(f"IP: {ip}", "magenta"))
        print(colored(f"Location: {city}", "magenta"))
        print(colored(f"Region: {region}", "magenta"))
        print(colored(f"Country: {country}", "magenta"))
        print(colored(f"Timezone: {timezone}", "magenta"))
        print()
        print(colored("Target set to " + ip + " using " + protocol + ".", "magenta",))
        print(colored("Starting attack with 16 threads, use CTRL+C to stop at any time", "magenta",))
        print()
        while True:
            mbSec = round(random.uniform(10, 40), 1)
            hitRate = round(random.uniform(95, 100), 2)
            curThread = random.randint(1, 16)
            if random.randint(1, 1000) < 10:
                print(colored("Thread {}: Thread underperforming or not responding, restarting...".format(curThread),"red",))
                print(colored("Thread {}: Thread successfully restarted. Attacking target...".format(curThread),"green",))
            else:
                print(colored("Thread {}: {}MB sent in the last second to target with a {}% Hitrate on requests.".format(curThread, mbSec, hitRate),"green",))
            time.sleep(0.1)
    else:
        print("Failed to fetch location data. Unable to proceed with the attack.")

def main():
    print()
    print(colored("Starting Echo Down!", "red"))
    print(colored("I am sure you are using this for legal purposes - Echo", "red"))
    print()

    with Halo(text=colored("Updating", "yellow"), spinner="dots") as h1:
        time.sleep(0.5)
        h1.succeed(colored(" Up to date", "green"))

    with Halo(text=colored("Starting Proxy", "yellow"), spinner="dots") as h7:
        time.sleep(0.5)
        h7.succeed(colored(" Proxy online", "green"))

    with Halo(text=colored("Starting!", "yellow"), spinner="dots") as h10:
        time.sleep(0.5)
        h10.succeed(colored(" Start", "green"))

    print(colored('''
            
 ███████╗░█████╗░██╗░░██╗░█████╗░  ██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗
 ██╔════╝██╔══██╗██║░░██║██╔══██╗  ██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║
 █████╗░░██║░░╚═╝███████║██║░░██║  ██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║
 ██╔══╝░░██║░░██╗██╔══██║██║░░██║  ██║░░██║██║░░██║░░████╔═████║░██║╚████║
 ███████╗╚█████╔╝██║░░██║╚█████╔╝  ██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║
 ╚══════╝░╚════╝░╚═╝░░╚═╝░╚════╝░  ╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝
       
''', 'red'))
    print(colored("                 The most powerful DDoS tool out there","red",attrs=["bold"],))
    print()
    menu_selections = [
        'Start',
        'Credits',
        'Exit'
    ]
    print('Pick an option...')
    for i, option in enumerate(menu_selections, start=1):
        print(f'{i}. {option}')
    menu_selection = input('> ')
    if menu_selection == '1':
        menu_selection = 'Start'
    elif menu_selection == '2':
        menu_selection = 'Credits'
    elif menu_selection == '3':
        menu_selection = 'Exit'
    else:
        print(colored("Error: Unknown response at python userInput, promise rejected", "red"))
        exit("userInput void")

    match menu_selection:
        case 'Start':
            print("Enter IP address:")
            ip = input(colored("> ", "yellow"))
            if not re.match(r"^(\d{1,3}\.){3}\d{1,3}$", ip):
                print(colored("Error: Invalid IP address format at python userInput, promise rejected", "red"))
                exit("userInput void")

            print("Select a protocol (TCP, UDP, or HTTP):")
            protocol = input(colored("> ", "yellow"))
            if protocol not in ['TCP', 'UDP','HTTP']:
                print(colored("Error: Invalid protocol at python userInput, promise rejected", "red"))
                exit("userInput void")

            city, country, region, timezone = get_location(ip)
            print(colored("Launching with 16 threads.", "cyan"))
            print()
            start_attack(ip, protocol, city, country, region, timezone)
        case 'Credits':
            print(colored('        ECHODOWN', 'red', attrs=['bold']))
            print(colored('''
    Star us on github!
    https://github.com/3kh0/echodown

    Developers
    @3kh0
    @aeiea
    @RuralAnemone
    @hackinghacker1
    ''', 'green'))
            exit(0)
        case 'Exit':
            exit(0)


if __name__ == "__main__":
    main()
