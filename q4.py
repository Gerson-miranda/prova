def calcular_preco (dis):
    if dis<=200:
        preco = dis*0.50
        
    else:
        preco =dis*0.45
    
    

    return preco

dis = int(input('digite a distancia da viagem  : '))


preco_a_pagar = calcular_preco(dis)

print(f' O proço da viagem vai ser de {preco_a_pagar}')