"""
44.	Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada.
Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo.
"""
altura_degrau = float(input('Digite a altura do degrau (cm): '))
altura_desejada = float(input('Digite a altura que você deseja alcançar (cm): '))
degraus_qtd = altura_desejada / altura_degrau
print(f'Você deverá subir {degraus_qtd} degraus')
