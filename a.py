def funcao(x):
    return x*x + 2*x + 1

vet = [1,2,3]
a = list(map(funcao, vet))
print(a)