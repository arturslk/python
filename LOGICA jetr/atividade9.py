h = float(input("digite sua altura"))
b = input("digite M para MASCULINO ou F para FEMININO")
if b == "M":
    c = (72.7*h) - 58
    print(c)
if b == "F":
    d = (62.1*h) - 44.1
    print(d)