# Programa para calcular o consumo de energia elétrica de um eletrodoméstico em um mês

equipamento = input("Qual é o seu eletrodomético: ")

potencia = float(input(f"Qual é a potência do(a) {equipamento} (em watts): "))

horas_por_dia = float(input("Quantas horas por dia o seu eletrodoméstico é utilizado ou fica ligado: "))

dias_por_mes = float(input("Quantos dias por mês o seu eletrodoméstico é utilizado ou fica ligado: "))

# Aqui é o calculo do o consumo de energia mensal

energia_mensal = (potencia * horas_por_dia * dias_por_mes) / 1000


custos_por_kwh = float(input("Qual é o custo do kWh em sua região (em reais): "))

# Aqui é o calculo do custo total em reais  do consumo de energia mensal
custo_total = energia_mensal * custos_por_kwh

print(f"A energia consumida pelo(a) {equipamento} em um mês é de {energia_mensal:.2f} kWh.")
print(f"O custo total do consumo de energia do(a) {equipamento} em um mês é de R$ {custo_total:.2f} reais.")
