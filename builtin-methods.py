message = 'corona vaccine is ready to use, most of them are more than 90% effective.'
print(message.capitalize())
print(message)
Message = message.capitalize()
print(Message)

# dir()
print(dir([]))

print(message.upper())
print(message.islower())
print(message.isupper())

print(message.find('ready'))
print(message[18:24])
print(message.find('not'))

seq1 = ('192', '168', '40', '90')
print('.'.join(seq1))
print('/'.join(seq1))

mountains = ['Everest', 'Himalaya', 'Sahyadri', 'Alps', 'K2', 'Mt Hood']
print(mountains)
mountains.append('Oregon mount')
print(mountains)
mountains.extend(['Mt Rainer', 'Satpuda'])
print(mountains)
mountains.insert(2, 'Mt Abu')
print(mountains)
mountains.pop()
mountains.pop()
mountains.pop()
print(mountains)
mountains.pop(5)
print(mountains)

cntr_emp1 = {'Name': 'Santa', 'Skill': 'Blockchain', 'Code': 1024}
print(cntr_emp1.keys())
print(cntr_emp1.values())
cntr_emp1.clear()
print(cntr_emp1)
