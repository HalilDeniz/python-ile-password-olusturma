import random
from termcolor import colored

lower   = "qwertyuıopğü,işlkjhgfdsa<zxcvbnmöç"
upper   = "QWERTYUIOPĞÜ,İŞLKJHGFDSAZXCVBNMÖÇ"
numbers = "1234567890"
symbols = "!'^+%&/()=?~'||\}][{¾½½$#$£>é_,.:;<>"
#topla = lower+upper+numbers+symbols
#uzunluk = 16

while True:
    try:
        topla = lower+upper+numbers+symbols
        uzunluk = random.randint(16,40)
        password = "".join(random.sample(topla,uzunluk))
        print(colored(f"\rDurdurmak için Ctrl+C: {password}","red"),end="")
    except KeyboardInterrupt:
        print(colored(f"\nÖnerilen Password: {password}","green"))
        print(colored(f"Uzunluk: {len(password)}","green"))
        break