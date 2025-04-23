
from string import ascii_letters

chars = {char: ord(char) for char in ascii_letters}
for  key, val in chars.items():
    print(f"{key}: {val}")