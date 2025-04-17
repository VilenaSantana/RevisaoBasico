a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))
#calcular o valor de A e B
soma = a + b
#verificar se o valor de C é maior que a soma de A e B
if c > soma:
    print(f"O terceiro número informado {c} é maior que a soma dos dois primeiros números {soma}")
else:
    print(f"O terceiro número informado {c} é menor que a soma dos dois primeiros números {soma}")