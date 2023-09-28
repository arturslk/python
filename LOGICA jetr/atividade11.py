valorCarro = 10000;

pagamento = int(input("carro = R$10000 forma de pagamento: \n 1 - dinheiro ou cheque \n 2 - cartão de crédito \n 3 - dividido em duas vezes \n 4 - dividido em duas vezes com juros"))

if(pagamento == 1):

	valorFinal = str(valorCarro - (valorCarro * 0.1))

	print ("o valor total será: " + valorFinal)

elif(pagamento == 2):

	valorFinal = str(valorCarro - (valorCarro * 0.15))
  
	print ("o valor total será: " + valorFinal)

if(pagamento==3):

	valorFinal = str(valorCarro - (valorCarro*0.1)/2)
   
	print("o valor total será:" + valorFinal)

elif(pagamento == 4):

	valorFinal = str(valorCarro - (valorCarro*0.1)/2 * 0.1)

	print("o valor total será:" + valorFinal)