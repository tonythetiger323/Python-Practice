planet1 = 'Closest to sun'
print(planet1)

print(planet1[0])
print(planet1[1])
print(planet1[2])

print(planet1[-1])
print(planet1[-2])
print(planet1[-3])

# Slicing a string
print(planet1[1:4])
print(planet1[:])
print(planet1[:7])
print(planet1[11:])

# Slicing tuple/list
devops = ('Linux', 'Vagrant', 'Bash', 'AWS', 'Jenkins', 'Python', 'Ansible')
print(devops[0])
print(devops[4])
print(devops[-1])

print(devops[2:5])
print(devops[2:5][0])
print(devops[2:5][0][:4])
print(devops[2:5][0][:4][-1])

# Dictionary
skills = {'devops': ('Linux', 'Vagrant', 'Bash', 'AWS', 'Jenkins', 'Python', 'Ansible'), 'development': ['java', 'nodejs', '.net']}
print(skills)
print(skills['devops'])
print(skills['development'])
print(skills['devops'][-1])
print(skills['devops'][-1][:3])