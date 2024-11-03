import requests
import os
import time
from colorama import Fore, Style, init
init(autoreset=True)

def grab_domains(api_url):
    while True:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            if "domains" in data and data["domains"] and "No data available" not in data["domains"]:
                return data["domains"]
            else:
                print(Fore.YELLOW + "No data")
                return []
        elif response.status_code == 502:
            print(Fore.RED + "Error: 502 - Retrying...")
            time.sleep(2)
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return []
def main():
    api_key = input("Enter API key: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    print("""       __                      _                 ___                                                             __    __             
  ____/ /___  ____ ___  ____ _(_)___        ____/ (_)_____________ _   _____  _______  __      ____ __________ _/ /_  / /_  ___  _____
 / __  / __ \/ __ `__ \/ __ `/ / __ \______/ __  / / ___/ ___/ __ \ | / / _ \/ ___/ / / /_____/ __ `/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
/ /_/ / /_/ / / / / / / /_/ / / / / /_____/ /_/ / (__  ) /__/ /_/ / |/ /  __/ /  / /_/ /_____/ /_/ / /  / /_/ / /_/ / /_/ /  __/ /    
\__,_/\____/_/ /_/ /_/\__,_/_/_/ /_/      \__,_/_/____/\___/\____/|___/\___/_/   \__, /      \__, /_/   \__,_/_.___/_.___/\___/_/     
                                                                                /____/      /____/                         
- domain discovery grabber project 
- made by eclibse security labs
- visit : https://eclipsesec.tech/\n""")
    print("[ 1 ] - Grab all [ recommended]")
    print("[ 2 ] - Grab by extension")
    choice = input("Choose: ").strip()
    base_url_all = f"https://eclipsesec.tech/api/?discovery=true&apikey={api_key}"
    base_url_by_extension = f"https://eclipsesec.tech/api/?discovery=true&apikey={api_key}&extension="
    if choice == "1":
        api_url = base_url_all
    elif choice == "2":
        extension = input("Enter extension (e.g., .id): ").strip()
        api_url = base_url_by_extension + extension
    else:
        print("Invalid choice.")
        return
    num_scrapes = int(input("Enter how many times to scrape: "))
    delay = float(input("Enter delay between requests (in seconds): "))
    for i in range(num_scrapes):
        print(Fore.CYAN + f"\n[Scraping Attempt {i+1}]")
        domains = grab_domains(api_url)
        if domains:
            count = len(domains)
            print(Fore.GREEN + f"{count} new domains found.")
            with open("result_discover.txt", "a") as file:
                for domain in domains:
                    file.write(domain + "\n")
            print(Fore.CYAN + "- New results saved to result_discover.txt")
        else:
            print(Fore.YELLOW + "No data")
        if i < num_scrapes - 1:
            time.sleep(delay)

if __name__ == "__main__":
    main()
