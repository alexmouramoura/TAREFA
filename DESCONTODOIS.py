
compra = float(input("Digite o valor da compra R$: "))

if compra < 200:
    desconto = compra * 0.05
elif compra < 300:
    desconto = compra * 0.10
else:
    desconto = compra * 0.15
""" calculando o preço final da compra após o desconto """
preco_final = compra - desconto

"""mostra qual foi o valor do desconto"""
print(f"O valor do desconto é R$: {desconto:.2f}")

"""mostra qual foi o valor final da compra após o desconto"""
print(f"O valor final da compra é R$: {preco_final:.2f}")