brt = float(input("digite seu salario bruto: "))

if brt <= 1903.98:
  print("Inseto")

if brt <= 2826.65:
  teor = brt * 0.50
  brt = brt - teor
  print("Seu salário é:", brt, "7,5%")

if brt <=3751.05:
  teor = brt * 0.15
  brt = brt - teor
  print("Seu salario é:", brt.teor, "15%")

elif brt <= 4664.68:
  teor = brt * 0.225
  bruto = brt - teor
  print("Seu salario é:", brt, "22.5%")

else:
  teor = brt * 0.275
  brt = brt - teor
  print("Seu salario é:", brt, "27.5%")