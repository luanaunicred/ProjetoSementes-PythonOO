class Caixa_Atacado:
    def __init__(self):
        self.produtos_cadastrados = []
        self.valor_total = 0

    def computar_compra(self, compra):
        texto_compra = compra.read()
        lista_compra = texto_compra.split('\n')

        tipo_pagamento = lista_compra[0].strip()
        lista_produtos = lista_compra[1:]

        compras = {}

        for item in lista_produtos:
            if item.strip():
                id_produto, quantidade = item.split(',')
                id_produto = int(id_produto)
                quantidade = int(quantidade)
                compras[id_produto] = compras.get(id_produto, 0) + quantidade

        for id_produto, quantidade in compras.items():
            for produto in self.produtos_cadastrados:
                if produto.id == id_produto:
                    valor_unitario = produto.valor_unitario
                    valor_total_produto = valor_unitario * quantidade

                    if quantidade >= 51:
                        desconto = 0.25
                    elif quantidade >= 21:
                        desconto = 0.20
                    elif quantidade >= 11:
                        desconto = 0.10
                    else:
                        desconto = 0.0

                    valor_total_produto *= (1 - desconto)
                    self.valor_total += valor_total_produto
                    break

        if tipo_pagamento.lower() == 'dinheiro':
            self.valor_total *= 0.95
        elif tipo_pagamento.lower() == 'credito':
            self.valor_total *= 1.03

    def adicionar_produto(self, produto):
        self.produtos_cadastrados.append(produto)
        print(f"Produto '{produto.nome}' adicionado ao estoque.")

    def exibir_valor_total(self):
        print(f"Valor Total: R$ {self.valor_total:.2f}")

class Produto:
    def __init__(self, id, nome, valor_unitario):
        self.id = id
        self.nome = nome
        self.valor_unitario = valor_unitario