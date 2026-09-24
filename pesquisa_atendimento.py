TOTAL_ENTREVISTADOS = 50

quantidade_excelente = 0
quantidade_ruim = 0

for numero in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\nEntrevistado {numero} de {TOTAL_ENTREVISTADOS}")

    nome = input("Digite o nome: ").strip()
    idade = int(input("Digite a idade: "))
    opiniao = input(
        "Digite sua opinião sobre o atendimento (EXCELENTE BOM ou RUIM): "
    ).strip().upper()

    if opiniao == "EXCELENTE":
        quantidade_excelente += 1
    elif opiniao == "RUIM":
        quantidade_ruim += 1

print("\nResultado da pesquisa:")
print(f"Quantidade de respostas EXCELENTE: {quantidade_excelente}")
print(f"Quantidade de respostas RUIM: {quantidade_ruim}")
