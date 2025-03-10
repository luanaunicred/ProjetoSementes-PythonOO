from Desafio_2.caixa_atacado import *

caixa = Caixa_Atacado()

p1 = Produto(1, 'Café 500g', 35.00)             # x 12 = 420.00 - 10% = 378.00
p2 = Produto(2, 'Pão 400g', 16.00)              # x 17 = 272.00 - 10% = 244.80
p3 = Produto(3, 'Queijo 150g', 12.00)           # x 32 = 384.00 - 20% = 307.20
p4 = Produto(4, 'Leite 1l', 5.00)               # x 28 = 140.00 - 20% = 112.00
p5 = Produto(5, 'Presunto 150g', 6.00)          # x 75 = 450.00 - 25% = 337.50
p6 = Produto(6, 'Manteiga 200g', 9.00)          # x 2  = 18.00

#total = 1397,50

caixa.adicionar_produto(p1)
caixa.adicionar_produto(p2)
caixa.adicionar_produto(p3)
caixa.adicionar_produto(p4)
caixa.adicionar_produto(p5)
caixa.adicionar_produto(p6)

# Abre o arquivo de compra e computa a compra
compra = open('compra.txt', 'r')
caixa.computar_compra(compra)
compra.close()

caixa.exibir_valor_total()

#final_dinheiro = 1327,62
#final_credito = 1439,42
#final_debito = 1397,50