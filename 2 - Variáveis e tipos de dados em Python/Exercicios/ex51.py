"""
51,	Escreva um programa que leia as coordenadas x e y de pontos no R2 e calcule sua distanciada origem (0,0).
"""
coord_x = int(input('Digite a coordenada x: '))
coord_y = int(input('Digite a coordenada y: '))
distancia_origem = (coord_x ** 2 + coord_y ** 2) ** 0.5
print(f'A distância da origem é de {distancia_origem:.2f} unidades')
