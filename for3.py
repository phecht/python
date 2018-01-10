"""This is a simple for loop with zip"""
PERSON_NAME = ['Alvin', 'Betty', 'Carl']
PERSON_DOMAIN = ['hotmail', 'live', 'google']

for name, domain in zip(PERSON_NAME, PERSON_DOMAIN):
    print(name, domain)
