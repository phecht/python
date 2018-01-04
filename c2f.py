def c2f(celsius):
    if type(celsius) != float:
        return -1
    if celsius < -273.15:
        return "invalid temp"
    return ((celsius * 9)/5)+32

celsius = input("Celsius:")

print(c2f(float(celsius)))