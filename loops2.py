import time

VACCINES = ['Moderna', 'Pfizer', 'Sputnik v', 'Covaxin', 'AstraZeneca']

for vac in VACCINES:
    print('')
    print('I would like to take a shot of')
    for i in vac:
        print(i)

x = 2
while True:
    print('Value of x is', x)
    print('Looping')
    x *= 2
    time.sleep(1)