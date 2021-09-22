print('Vamos construir um triângulo?')
print('Obs: Importante não inserir o valor 0!')
x = int(input('Digite um valor inteiro qualquer: '))
y = int(input('Digite um segundo valor inteiro qualquer: '))
z = int(input('Digite um terceiro valor inteiro qualquer: '))
if (x == y) and (y == z) and (x == z):
    print('Triângulo Equilátero')
if (x == y) or (x == z) or (y == z):
    print('Triângulo Isósceles')
if (x != y) and (x != z) and (y != z):
    print('Triângulo Escaleno')
