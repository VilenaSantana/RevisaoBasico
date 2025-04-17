p = float(input("Qual seu peso? "))
a = float(input("Qual sua altura? "))
imc = p/(a*a)
if imc < 18.6:
    print("Você está abaixo do peso.")
elif imc >= 18.6 and imc < 24.9:
    print("Você está no peso ideal. Parabéns!")
elif imc >= 25 and imc < 29.9:
    print("Você está levemente acima do peso.")
elif imc >= 30 and imc < 34.9:
    print("Você está obesidade grau I.")
elif imc >= 35 and imc < 39.9:
    print("Você está obesidade grau II. Obesidade SEVERA!")
else:
    print("Você está obesidade grau III. Obesidade MÓRBIDA!")
