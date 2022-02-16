from random import choice, randint
from time import sleep
import requests
fout = open ('log.txt', 'w')
chara = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


link = []
invalid = 0
valid = 0

print("Press Ctrl-C to quit.")

while True:
    try:
        for i in range(randint(10,16):
            c = choice(chara)
            if chara.index(c) < 25:
                if randint(0, 1) == 1):
                    link.append(str(c).capitalize())
                else:
                    link.append(c)
            else:
                link.append(c)
        code = ''.join(link)
        api = requests.get(f'https://discord.com/api/v8/entitlements/gift-codes/{code}')
        if (int(api.status_code) == 200):
            fout.write(f'https://discord.gift/{code} is valid!\n')
            valid += 1
        if (int(api.status_code) == 429):
            fout.write("Too many requests! https://discord.gift/{code}\n")
            invalid += 1
        else:
            fout.write(f'https://discord.gift/{code} is invalid!\n')
            invalid += 1
            
    except KeyboardInterrupt:
        break

fout.close()

print(f"{invalid+valid} codes checked. {valid} valid codes found. {invalid} invalid codes found.")

