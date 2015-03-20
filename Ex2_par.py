#Ex2_par

def par(x):
    r=x%2
    if r==0:
        print("O numero eh par!")
    else:
        print("O numero nao eh par!")

print("Teste do numero par:\n")
x=int(input("Digite o valor do numero: "))
par(x)
input()
