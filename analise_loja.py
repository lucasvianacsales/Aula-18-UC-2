import base_loja

listaVendas = base_loja.vendas["vendas"]

print(f"Quantidade de Vendas: {len(listaVendas)}")

totalUnidades = 0
for venda in listaVendas:
    totalUnidades += venda["quantidade"]

print(f"Total de Unidades Vendidas: {totalUnidades}")