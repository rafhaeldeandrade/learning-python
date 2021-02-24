"""
45. Faça um algoritmo que converta uma velocidade expressa em km/ h para m/s e vice versa.
Você deve criar um menu com as duas opções de conversão e com uma opção para sair.
O usuário poderá fazer quantas conversões desejar, sendo que o programa só será finalizado 
quando a opção de finalizar for escolhida.
"""
while True:
    menu = input("""Digite 1 para converter uma velocidade em km/h para m/s
Digite 2 para converter uma velocidade em m/s para km/h
Digite 3 para finalizar o programa
Sua opção: """)

    if menu == '1':
        velocidade = float(input('Digite a velocidade em km/h: '))
        print(f'{(velocidade / 3.6):.2f} m/s')
    elif menu == '2':
        velocidade = float(input('Digite a velocidade em m/s: '))
        print(f'{(velocidade * 3.6):.2f} km/h')
    elif menu == '3':
        print('Finalizando.')
        break
    else:
        print('Valor errado, digite 1, 2 ou 3.')
