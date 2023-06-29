import random

# Break
for i in 'DevOps':
    print(i)
    if i == 'O':
        print('Found data')
        break
print('Out of loop')

# Continue
for i in 'DevOps':
    if i == 'O':
        print('Found data')
        continue
    print(f'Value of i: {i}')
print('Out of loop')

# Break and continue
# VACCINES = ['Moderna', 'Pfizer', 'Sputnik v', 'Covaxin', 'AstraZeneca']
#
# random.shuffle(VACCINES)
# print(VACCINES)
#
# LUCKY = random.choice(VACCINES)
# print(LUCKY)
#
# for vac in VACCINES:
#     print(f'Testing Vaccine: {vac}')
#     if vac == LUCKY:
#         print('#################################')
#         print(f'{LUCKY} vaccine test successful!')
#         print('#################################')
#         break
#     print('XXXXXXXXXXXX')
#     print('Test failed!')
#     print('XXXXXXXXXXXX')

VACCINES = ['Moderna', 'Pfizer', 'Sputnik v', 'Covaxin', 'AstraZeneca']

random.shuffle(VACCINES)
print(VACCINES)

LUCKY = random.choice(VACCINES)
print(LUCKY)

for vac in VACCINES:
    print(f'Testing Vaccine: {vac}')
    if vac == LUCKY:
        print('#################################')
        print(f'{LUCKY} vaccine test successful!')
        print('#################################')
        continue
    print('XXXXXXXXXXXX')
    print('Test failed!')
    print('XXXXXXXXXXXX')
