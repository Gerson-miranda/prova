# # limite = 80.00

# # multa = 5.00

# # velocidade = int(input('digite a velocidade percorrida : '))

# # excesso =(velocidade - limite)
# # pagar = (excesso * multa )

# # if excesso<=limite :
# #     print(f' O valor da  multa vai ser de  {pagar :.2f}')
    
# # else:
# #     print('Não vai pagar multa')



# def calcular_media(num1,num2,num3):
#     media =(num1+num2+num3)//3
#     return media


# def resultado(m):
#     if(m>=7):
#         print('você foi aprovado')
        
#     else:
#         print('você foi reprovado')
        
# num1= float(input('digite a primeira nota : '))
# num2= float(input('digite a segunda  nota : '))
# num3= float(input('digite a terceira nota : '))

# media = calcular_media(num1,num2,num3)    

# resultado(media)       
     


# num1= float(input('digite a primeira nota : '))
# num2= float(input('digite a segunda  nota : '))
# num3= float(input('digite a terceira nota : '))

# media = (num1 + num2 + num3)/3

# if (media >= 7):
#     print(f'você foi aprovado! e sua media foi de {media :.2f}')
    
# if (media >= 5 and media<=6.9):
#     print(f'você ta na recuperação! e sua media foi de {media :.2f}')
    
# else:
#     print(f'você foi esta reprovado ! e sua media foi de {media :.2f}')


def calcular_preco (dis):
    if dis<=200:
        preco = dis*0.50
        
    else:
        preco =dis*0.45
    
    

    return preco

dis = int(input('digite a distancia da viagem  : '))

preco_a_pagar = calcular_preco(dis)



    












