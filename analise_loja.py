import base_loja

maior_valor = 0
menor_valor = 999999
total_vendas = 0
media_vendas = 0
n_vendasmaior = 0

for venda in base_loja.vendas["vendas"]:
    valor_total = venda["quantidade"]*venda["valor_unitario"]

    if valor_total > maior_valor:
        maior_valor = valor_total
    
    if valor_total < menor_valor:
        menor_valor = valor_total

    total_vendas += valor_total

    if valor_total > 5000:
        n_vendasmaior += 1

media_vendas = total_vendas/len(base_loja.vendas["vendas"])
        
print(f"Maior venda: R$ {maior_valor:.2f}")
print(f"Menor venda: R$ {menor_valor:.2f}")
print(f"Total de vendas: R$ {total_vendas:.2f}")
print(f"Média das vendas: R$ {media_vendas:.2f}")
print(f"Número de vendas acima de 5000: {n_vendasmaior}")
