from random import choice, randint
import requests
fout = open ('log.txt', 'w')
chara = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

link = []
for i in range(16):
    x = random.choice(chara)
    if (chara.index(x) < 25):
        if (randint(0, 1) == 1):
            link.append(str(x).capitalize())
        else:
            link.append(x)
    else:
        link.append(x)
code = ''.join(link)
api = requests.get(f'https://discord.com/api/v8/entitlements/gift-codes/{code}')
if (int(api.status_code) == 200):
    fout.write(f'https://discord.gift/{code} is valid!\n')
if (int(api.status_code) == 429):
    fout.write("Too many requests! https://discord.gift/{code}\n")
else:
    fout.write(f'https://discord.gift/{code} is invalid!\n')
    
fout.close()
