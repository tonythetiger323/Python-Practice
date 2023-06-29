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

vac_feedback('Pfizer', 95)
vac_feedback('Unknown', 45)
vac_feedback(efficacy = 34, vac = 'J&J')
