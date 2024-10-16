limite = 80.00

multa = 5.00

velocidade = int(input('digite a velocidade percorrida : '))

excesso =(velocidade - limite)
pagar = (excesso * multa )

if velocidade>limite :
    print(f' O valor da  multa vai ser de  {pagar :.2f}')
    
else:
    print('Não vai pagar multa')