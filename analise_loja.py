import base_loja

maior_valor = 0
total_vendas = 0

for venda in base_loja.vendas["vendas"]:
    valor_total = venda["quantidade"]*venda["valor_unitario"]

    if valor_total > maior_valor:
        maior_valor = valor_total

    
        
print("Maior venda")
print(f"Valor total: R$ {maior_valor:.2f}")

