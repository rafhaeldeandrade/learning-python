"""
39.	Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela
que considera o salário atual e o tempo de serviço de cada funcionário. Os funcionários com menor
salário terão um aumento proporcionalmente maior do que os funcionários com um salário maior,
e conforme o tempo de serviço na empresa, cada funcionário irá receber um bónus adicional de salário.
Faça um programa que leia:
*	o valor do salário atual do funcionário;
*	o tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa).

Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do salário final reajustado,
ou uma mensagem caso o funcionário não tenha direito a nenhum aumento.

Salário atual       Reajuste        Tempo de serviço    Bônus
até R$500,00        25%             abaixo de 1 ano     sem bônus
até R$1000,00       20%             de 1 a 3 anos       R$100,00
até R$1500,00       15%             de 4 a 6 anos       R$200,00
até R$2000,00       10%             de 7 a 10 anos      R$300,00
acima de 2000,00    sem reajuste    mais de 10 anos     R$500,00
"""
salario_atual = float(input('Digite o salário atual do funcionário: '))
tempo_servico = int(input('Digite o número de anos trabalhado do funcionário: '))

if salario_atual <= 500:
    if tempo_servico < 1:
        salario_reajustado = salario_atual + salario_atual * 0.25
    elif tempo_servico <= 3:
        salario_reajustado = salario_atual + salario_atual * 0.25 + 100
    elif tempo_servico <= 6:
        salario_reajustado = salario_atual + salario_atual * 0.25 + 200
    elif tempo_servico <= 10:
        salario_reajustado = salario_atual + salario_atual * 0.25 + 300
    else:
        salario_reajustado = salario_atual + salario_atual * 0.25 + 500
elif salario_atual <= 1000:
    if tempo_servico < 1:
        salario_reajustado = salario_atual + salario_atual * 0.2
    elif tempo_servico <= 3:
        salario_reajustado = salario_atual + salario_atual * 0.2 + 100
    elif tempo_servico <= 6:
        salario_reajustado = salario_atual + salario_atual * 0.2 + 200
    elif tempo_servico <= 10:
        salario_reajustado = salario_atual + salario_atual * 0.2 + 300
    else:
        salario_reajustado = salario_atual + salario_atual * 0.2 + 500
elif salario_atual <= 1500:
    if tempo_servico < 1:
        salario_reajustado = salario_atual + salario_atual * 0.15
    elif tempo_servico <= 3:
        salario_reajustado = salario_atual + salario_atual * 0.15 + 100
    elif tempo_servico <= 6:
        salario_reajustado = salario_atual + salario_atual * 0.15 + 200
    elif tempo_servico <= 10:
        salario_reajustado = salario_atual + salario_atual * 0.15 + 300
    else:
        salario_reajustado = salario_atual + salario_atual * 0.15 + 500
elif salario_atual <= 2000:
    if tempo_servico < 1:
        salario_reajustado = salario_atual + salario_atual * 0.1
    elif tempo_servico <= 3:
        salario_reajustado = salario_atual + salario_atual * 0.1 + 100
    elif tempo_servico <= 6:
        salario_reajustado = salario_atual + salario_atual * 0.1 + 200
    elif tempo_servico <= 10:
        salario_reajustado = salario_atual + salario_atual * 0.1 + 300
    else:
        salario_reajustado = salario_atual + salario_atual * 0.1 + 500
else:
    if tempo_servico < 1:
        salario_reajustado = salario_atual + salario_atual
    elif tempo_servico <= 3:
        salario_reajustado = salario_atual + salario_atual + 100
    elif tempo_servico <= 6:
        salario_reajustado = salario_atual + salario_atual + 200
    elif tempo_servico <= 10:
        salario_reajustado = salario_atual + salario_atual + 300
    else:
        salario_reajustado = salario_atual + salario_atual + 500

print(f'Salário atual: R${salario_atual:.2f}\nSalário depois do reajuste: R${salario_reajustado:.2f}')
