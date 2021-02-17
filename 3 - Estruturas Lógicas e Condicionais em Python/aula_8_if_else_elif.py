"""
Estruturas condicionais 
IF, ELSE, ELIF

#Estrutura condicional if/else/else if em C
if(idade < 18){
    printf('Menor de idade');
}else if(idade == 18){
    printf('Tem 18 anos');
}else{
    printf('Maior de idade');
}

#Estrutura condicional if/else/else if em Java
if(idade < 18){
    System.out.println('Menor de idade');
}else if(idade == 18){
    System.out.println('Tem 18 anos');
}else{
    System.out.println('Maior de idade');
}
"""

idade = 18

#não há necessidade de colchetes, abre o bloco com : [dois pontos] e idente com 4 espaços para o bloco correspondente
if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
else:
    print('Maior de idade')
