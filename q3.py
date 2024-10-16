salario = int(input('Digite o seu salario:'))

casa = int(input('Digite o valor da  casa:'))

anos_a_pagar = int(input('Digite a quantidade de  anos_a_pagar :'))

qprest = anos_a_pagar*12

prestacao = casa/qprest

if (prestacao>salario*0.30):
    print('infelizmente o você não pode obter o empréstimo  ')
    
else :
    print(f'Emprestimo ok, você vai pagar de prestação R$ {prestacao :.2f}')