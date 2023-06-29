print('This IT Organization has various skill sets.')
print('Find your match')

print('Enter Capitalized Values:')

DevOps = ['Jenkins', 'Ansible', 'Bash', 'Python', 'Puppet', 'Docker', 'Kubernetes', 'Terraform']
Development = ('Nodejs', 'Reactjs', 'Java', '.net', 'Python')
cntr_emp1 = {'Name': 'Santa', 'Skill': 'Blockchain', 'Code': 1024}
cntr_emp2 = {'Name': 'Santa', 'Skill': 'AI', 'Code': 1218}

usr_skill = input('Enter your desired skill: ')

# Check in the database if we have this skill
if usr_skill in DevOps:
    print(f'We have {usr_skill} in DevOps team')
elif usr_skill in Development:
    print(f'We have {usr_skill} in Development team')
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print('We have contract employees with this skill')
else:
    print('Skill not found')
    print('Please check if you have entered value capitalized or check the spelling')
