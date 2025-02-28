import json

class Produto:
    def __init__(self, id, nome, quantidade, preco):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def calcular_valor_total(self):
        return self.quantidade * self.preco

    def mostrar_informacoes(self):
        return f"ID: {self.id}, Nome: {self.nome}, Quantidade: {self.quantidade}, Preço: R${self.preco:.2f}"

class Mercado:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f"Produto '{produto.nome}' adicionado ao estoque.")

    def calcular_valor_total_estoque(self):
        total = 0
        for produto in self.produtos:
            total += produto.calcular_valor_total()
        return total

    def mostrar_estoque(self):
        print("\n--- Estoque do Mercado ---")
        for produto in self.produtos:
            print(produto.mostrar_informacoes())
        print(f"\nValor total em estoque: R${self.calcular_valor_total_estoque():.2f}")

