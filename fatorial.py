x = int(input("escolha um número: "))
def fatorial(x):
    if x == 1:
        return 1
    else:
        return x * fatorial(x-1)

print(fatorial(x))
