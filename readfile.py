file = open('fruits.txt','r')
cont = file.readlines()
file.close()

for line in cont:
    print(len(line)-1)