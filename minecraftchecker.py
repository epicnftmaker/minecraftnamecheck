import requests
import json
import colorama
from colorama import Fore

file_path = "usernames.txt"

print('''
minecraft username checker

i put no effort into this bit but it works so suck my meat thank u
      
made by epicnftmaker      ''')


with open(file_path, 'r') as file:
    for line in file:
        username = line.strip()
        url = f'https://api.minetools.eu/uuid/{username}'

        response = requests.get(url)
        response_data = json.loads(response.text)

        if response_data.get("status") == 'OK':
            print(f"Username {username}: Taken")
        else:
            with open("valid.txt", 'a') as valid_file:
                valid_file.write(username + "\n")
            print(f"Username {username}: Avaliable")
