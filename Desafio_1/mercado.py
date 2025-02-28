class Mercado:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)
        print(f"Produto '{produto.nome}' adicionado ao estoque.")

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.id, produto.nome, produto.quantidade, produto.valor)

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



class Produto:
    def __init__(self, id, nome, quantidade, valor):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor

    def calcular_valor_total(self):
        return self.quantidade * self.valor

    def mostrar_informacoes(self):
        return (f"ID: {self.id}, "
                f"Nome: {self.nome}, "
                f"Quantidade: {self.quantidade}, "
                f"Valor Unitário: R${self.valor:.2f}, "
                f"Valor Total: R${self.calcular_valor_total():.2f}")