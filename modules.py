import random

def vac_feedback(vac, efficacy):
    print(f'{vac} vaccine is {efficacy}% effective')
    if (efficacy > 50) and (efficacy <= 75 ):
        print('Seems not so effective, needs more trial')
    elif (efficacy > 75) and (efficacy < 90):
        print('Can consider')
    elif (efficacy >= 90):
        print('Approved for use')
    else:
        print('Needs a lot more testing and trial')

def orderFood(minOrd, *args):
    print(f'You have ordered: {minOrd}')
    # print(args)
    for item in args:
        print(f'You have ordered: {item}')
    print('Should be delivered in 30 mins')

def time_activity(*args, **kwargs):
    # print(args)
    # print(kwargs)
    min = sum(args) + random.randint(0, 60)
    # print(min)
    choice = random.choice(list(kwargs.keys()))
    # print(choice)
    print(f'You have to spend {min} minutes for {kwargs[choice]}')
