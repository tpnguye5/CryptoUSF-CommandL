import random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

key = ''.join(random.sample(letters, len(letters)))
print(key)