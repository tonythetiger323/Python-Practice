# Non keyword arguments
def orderFood(minOrd, *args):
    print(f'You have ordered: {minOrd}')
    # print(args)
    for item in args:
        print(f'You have ordered: {item}')
    print('Should be delivered in 30 mins')

orderFood('salad', 'pizza', 'biryani', 'soup')

