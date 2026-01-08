import base_loja

# maior_valor = 0
# menor_valor = 999999
# total_vendas = 0
# media_vendas = 0
# n_vendasmaior = 0

# for venda in base_loja.vendas["vendas"]:
#     valor_total = venda["quantidade"]*venda["valor_unitario"]

#     if valor_total > maior_valor:
#         maior_valor = valor_total
    
#     if valor_total < menor_valor:
#         menor_valor = valor_total

#     total_vendas += valor_total

#     if valor_total > 3000:
#         n_vendasmaior += 1

# media_vendas = total_vendas/len(base_loja.vendas["vendas"])
        
# print(f"Maior venda: R$ {maior_valor:.2f}")
# print(f"Menor venda: R$ {menor_valor:.2f}")
# print(f"Total de vendas: R$ {total_vendas:.2f}")
# print(f"Média das vendas: R$ {media_vendas:.2f}")
# print(f"Número de vendas acima de 5000: {n_vendasmaior}")

# lista_vendas = base_loja.vendas["vendas"]
# total_sudeste = 0
# for venda in lista_vendas:
#     if venda["regiao"] == "Sudeste":
#         total_sudeste = venda["quantidade"]*venda["valor_unitario"]
# print(f"Total de vendas no Sudeste: {total_sudeste:.2f}")

# nome_vendedores = []

# lista_vendas = base_loja.vendas["vendas"]

# for venda in lista_vendas:
#     if venda["vendedor"] not in nome_vendedores:
#         nome_vendedores.append(venda["vendedor"])

# nome_vendedores.sort()
# print(f"Quantidade de vendedores: {len(nome_vendedores)}")
# for vendedor in nome_vendedores:
#     print(vendedor)

# nome_regiao = []

# lista_vendas = base_loja.vendas["vendas"]

# for venda in lista_vendas:
#     if venda["regiao"] not in nome_regiao:
#         nome_regiao.append(venda["regiao"])
    
# nome_regiao.sort()
# print(f"Quantidade de regiões: {len(nome_regiao)}")
# for regiao in nome_regiao:
#     print(regiao)

# # Quantidade vendida por regiões

# lista_vendas = base_loja.vendas["vendas"]

# nome_regiao = []

# for venda in lista_vendas:
#     regiao = venda["regiao"]
#     if regiao not in nome_regiao:
#         nome_regiao.append(regiao)

# for regiao in nome_regiao:
#     valor_total_regiao = 0
#     for venda in lista_vendas:    
#         if venda["regiao"] == regiao:
#             valor_venda = venda["quantidade"]*venda["valor_unitario"]
#             valor_total_regiao = valor_total_regiao + valor_venda
#     print(f"Nome da região: {regiao}")
#     print(f"Valor total vendido: R$ {valor_total_regiao}")

# Utilizando dicionário

lista_vendas = base_loja.vendas["vendas"]

valor_total_regiao = {}

for venda in lista_vendas:
    regiao = venda["regiao"]
    valor_venda = venda["quantidade"]*venda["valor_unitario"]
    if regiao in valor_total_regiao:
        valor_total_regiao[regiao] = valor_total_regiao[regiao] + valor_venda
    else:
        valor_total_regiao[regiao] = valor_venda

print(valor_total_regiao)