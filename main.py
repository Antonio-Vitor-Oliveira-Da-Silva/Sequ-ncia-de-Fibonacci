qntSeg = int(input('Digite a quantidade de números: '))
x0 = 0 # Numero Anterior = 3
x1 = 1 # Numero Atual = 5
x = 1 # Numero Desconhecido = '?'
somaFibo = x0 + x1
print(x0, x1, end=' ')
for i in range(qntSeg):
    x = x1 + x0
    somaFibo += x
    print(x, end=' ')
    x0 = x1
    x1 = x
print(f'A soma dos {qntSeg} primeiros números é: {somaFibo}')