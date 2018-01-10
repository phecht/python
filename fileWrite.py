numbers = [1, 2, 3]
writeNumbers=open("numbers.txt","w")

for n in numbers:
    writeNumbers.write(str(n)+"\n")

writeNumbers.close()