casa = "casa" 
comercial = "comercial" 
apartamento = "apartamento"
 

tipo_imovel = input(f"qual é o seu tipo de imóvel é {casa}, {comercial} ou {apartamento}?: ")
 
consumo = float(input("qual o consumo mensal de água do seu imóvel m³: "))
 


if tipo_imovel == casa and consumo <= 25:
    print("consumo moderado dentro do padrão residencial")

elif tipo_imovel == comercial:
    print("tarifa comercial aplicada, consulte o plano corporativo para mais informações")

 
