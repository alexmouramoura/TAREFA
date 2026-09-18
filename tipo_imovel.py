TIPOS_VALIDOS = {"casa", "apartamento", "loja"}

imovel = input("Qual é o seu tipo de imóvel (casa, apartamento ou loja)? ").strip().lower()

if imovel not in TIPOS_VALIDOS:
    print("Tipo de imóvel inválido.")

elif imovel == "loja":

    print("Tarifa comercial aplicada, consulte o plano corporativo para mais informações.")

else:
    try:
        consumo = float(input("Qual é o consumo mensal de água do seu imóvel em m³? "))
    except ValueError:
        print("Consumo inválido. Informe um valor numérico.")
    else:
        if consumo <= 25:
            print("Consumo moderado dentro do padrão residencial.")
        else:
            print("Consumo acima do padrão residencial.")

        if consumo > 25:
            print("Consumo excessivo, considere revisar seus hábitos de consumo e verificar possíveis vazamentos.")

        if imovel == "apartamento" and consumo <= 10:
            print("Consumo econômico, excelente controle de água.")
