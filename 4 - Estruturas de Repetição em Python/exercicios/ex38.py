"""
38. Faça um programa que calcule o terno pitagórico a, b, c para o a + b + c = 1000
Um terno pitagórico é um conjunto de tres números naturais, a, b, c, para a qual,
a ^ 2 + b ^ 2 = c ^ 2
Por exemplo: 3 ^ 2 + 4 ^ 2 = 5 ^ 2
"""
for i in range(1, 999):
    for j in range(1, 999):
        for k in range(1, 999):
            if i + j + k == 1000:
                if (i ** 2 + j ** 2) == k ** 2:
                    print(f'{i ** 2} + {j ** 2} = {k ** 2}')
