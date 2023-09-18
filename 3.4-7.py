import random

guests = ['Matthew', 'Mariella', 'Szymon', 'Kay', 'Lazar', 'Mircea']

for i in guests:
    print(f'Hi {i}, would you like to come to my party?')

print('Kay can no longer come, I will invite Jaden instead.')

guests = ['Matthew', 'Mariella', 'Szymon', 'Jaden', 'Lazar', 'Mircea']

for i in guests:
    print(f'Hi {i}, would you like to come to my party?')

print('I have found a bigger table, I will invite more people.')

guests.append('Ruairi')
guests.append('Sam Wells')

for i in guests:
    print(f'Hi {i}, would you like to come to my party?')

print('I can only invite two people... Sorry')

while len(guests) > 2:
    choice = random.randint(1, len(guests))
    guests.pop(choice - 1)

print(guests)
print(len(guests))
