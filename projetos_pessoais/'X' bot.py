print('Olá, me chamo X, sou um bot em aprendizado.')
print('Qual o seu nome?')
nome = input('>: ')
print(f'Prazer em te conhecer {nome}!')
print('Como você está se sentindo?')
condicao = input('>: ')
condicoes = ['Bem', 'bem', 'Ótimo', 'ótimo', 'Otimo', 'otimo', 'Legal', 'legal', 'Bom', 'bom', 'Bão', 'bão', 'Suave',
             'suave', 'De boa', 'de boa', 'tranquilo', 'Tranquilo', 'Ótima', 'ótima', 'Otima', 'otima']
if condicao in condicoes:
        condicao_usuario = 'Fico feliz em saber disso =)'
else:
         condicao_usuario = 'Relaxa, as coisas vão melhorar ;)'
print(condicao_usuario)
tem_amigos = input('Você tem amigos? ')
if tem_amigos == "sim" and "Sim":
    quantidade_amigos = int(input('Que legal, quantos? '))
elif tem_amigos == "Sim" and "sim":
    quantidade_amigos = int(input('Que legal, quantos? Em número por favor. '))
else:
    print('Bem, quem sabe podemos ser amigos =)')
print()
if quantidade_amigos <= 3:
    print('Podem parecer poucos, mas com certeza são os melhores!!!')
elif quantidade_amigos >= 10:
    print('Oooowww... Temos uma pessoa popular aqui!')
elif quantidade_amigos == 4:
    print('O quarteto fantastico!!!')
print()
print('Por enquanto é isso... Acho que é hora de dar "Tchau"')
resposta = input('>: ')
if resposta == 'Tchau':
    print('Tchau tchau!')
quit()
