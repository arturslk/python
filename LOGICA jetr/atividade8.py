a = int(input("Digite um valor"))
b = int(input("Digite um segundo valor"))
c = int(input("Digite um terceiro valor"))
if a > b and b > c:
    print(a,b,c)
if b > a and a > c:
    print(b,a,c)
if c > a and a > b:
    print(c,a,b)
if b > c and c > a:
    print(b,c,a)
if a > c and c > b:
    print(a,c,b)
else: 
    if c > b and b > a:
     print(c,b,a)