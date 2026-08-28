from soma import somaf
from subtrai import subtraif
from multiplica import multiplicaf
from divide import dividef
from resto import restof

def main():
    n1 = int(input('Digite um número inteiro:'))
    n2 = int(input('Digite outro número inteiro:'))
    op = input('digite a operação:')
    if op == "+":
        print(somaf(n1,n2))
    elif op == "-":
        print(subtraif(n1, n2)) 
    elif op == "/":
        print(dividef(n1, n2))
    elif op == "*":
        print(multiplicaf(n1, n2))
    elif op == "%":
        print(restof(n1,n2))

main()
