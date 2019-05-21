list_char_1 = ['H', 'e', 'l', 'l', 'o']
list_char_2 = ['W', 'e', 'l', 'c', 'o', 'm', 'e']
list_char_4 = ['N', 'o', 'w', ', ', 'd', 'o', ' ', 'w', 'e', ' ', 'u', 'n', 'd', 'e', 'r', 's', 't', 'a', 'n', 'd']
list_char_5 = ['H', 'o', 'w', ',', ' ', '\\r', ' ', 'w', 'o', 'r', 'k', 's', '?']

import time

for ch in list_char_1:
	print(ch, end='', flush=True)
	time.sleep(0.5)

print('\r', end='', flush=True)

for ch in list_char_2:
	print(ch, end='', flush=True)
	time.sleep(0.5)

print('\r', end='', flush=True)

for ch in list_char_4:
	print(ch, end='', flush=True)
	time.sleep(0.5)

print('\r', end='', flush=True)

for ch in list_char_5:
	print(ch, end='', flush=True)
	time.sleep(0.5)

print('       ')
