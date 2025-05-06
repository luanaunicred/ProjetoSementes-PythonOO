import json
from mercado import Mercado, Produto


mercado = Mercado()

with open('produtos.json.py', 'r', encoding='utf-8') as file:
    lista_produtos = json.load(file)

for item in lista_produtos:
    produto = Produto(
        id=item["id"],
        nome=item["nome"],
        quantidade=item["quantidade"],
        valor=item["valor"]
    )
    mercado.inserir_produto(produto)

mercado.lista_produto()

print(f"\nValor total do estoque: R${mercado.calcular_valor_total_estoque():.2f}")