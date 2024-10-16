num1= float(input('digite a primeira nota : '))
num2= float(input('digite a segunda  nota : '))
num3= float(input('digite a terceira nota : '))

media = (num1 + num2 + num3)/3

if (media >= 7):
    print(f'você foi aprovado! e sua media foi de {media :.1f}')
    
if (media >= 5 and media<=6.9):
    print(f'você ta na recuperação! e sua media foi de {media :.1f}')
    
else:
    print(f'você foi esta reprovado ! e sua media foi de {media :.1f}')