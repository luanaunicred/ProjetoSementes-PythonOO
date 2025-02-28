from mercado import (Mercado)
from mercado import (Produto)

mercado = Mercado()

p1 = Produto(1,'Arroz', 50, 20.99)                      #1.049,50
p2 = Produto(2, 'Feijão', 30, 8.50)                     #255,00
p3 = Produto(3,'Macarrão', 40, 5.90)                    #236,00
p4 = Produto(4,'Açucar', 25, 4.20)                      #105,00
p5 = Produto(5, 'Café', 60, 4.20)                       #252,00
p6 = Produto(6, 'Leite', 100, 4.80)                     #480,00
p7 = Produto(7, 'Óleo de Soja', 70, 9.50)               #665,00
p8 = Produto(8, 'Sabonete', 200, 1.50)                  #300,00
p9 = Produto(9, 'Detergente', 150, 2.3)                 #345,00
p10 = Produto(10, 'Papel Higiênico', 80, 12.00)         #960,00

mercado.inserir_produto(p1)
mercado.inserir_produto(p2)
mercado.inserir_produto(p3)
mercado.inserir_produto(p4)
mercado.inserir_produto(p5)
mercado.inserir_produto(p6)
mercado.inserir_produto(p7)
mercado.inserir_produto(p8)
mercado.inserir_produto(p9)
mercado.inserir_produto(p10)

mercado.lista_produto()
print(mercado.lista_produto())

mercado.calcular_valor_total_estoque()
print(mercado.calcular_valor_total_estoque())

#valor total 4.647,50