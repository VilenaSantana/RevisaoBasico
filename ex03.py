p = "s"
while p == "s":
    n1 = float(input("Digite um número: "))
    if n1 < 0:
        if n1%2 == 0:
            print(f"O número {n1} è par e negativo")
        else:
            print(f"O número {n1} è impar e negativo")
    else:
        if n1%2 == 0:
            print(f"O número {n1} è par e positivo")
        else:
            print(f"O número {n1} è impar e positivo")
    p = input("Deseja fazer novamente? s ou n ")
else:
    print("Volte sempre")