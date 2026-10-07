salario = input("Digite o salário do funcionário: ")

# Limpa o valor digitado
salario = salario.replace("R$", "").replace(".", "").replace(",", ".")

salario = float(salario)

aumento = salario * 0.15
novo_salario = salario + aumento

print(f"Salário atual: R${salario:.2f}")
print(f"Aumento (15%): R${aumento:.2f}")
print(f"Novo salário: R${novo_salario:.2f}")