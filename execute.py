while 1:
  print('vamos calcular!\nDigite dois números e a operação desejada')
  num1 = float(input('digite um número: '))
  num2 = float(input('digite um número: '))
  soma = int(input('1 adição\n2 subtração\n3 multiplicação\n4 divisão\n'))
  if soma >=5:
    print('opçao invalida')
  elif soma == 1:
    print('resposta: ',num1 + num2)
  elif soma == 2:
    print('resposta: ',num1 - num2)
  elif soma == 3:
    print('resposta: ',num1 * num2)
  elif soma == 4:
    print('resposta: ',num1 / num2)
  sair = int(input('1 continuar\n2 sair\n'))
  if sair ==2:
    print('Até logo!')
    break
