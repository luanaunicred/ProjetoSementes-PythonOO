from biblioteca import *

class Menu:
    def menu(self):
        biblioteca = Biblioteca()

        while True:
            print('\nGestão da Biblioteca:')
            print('1. Adicionar um novo livro')
            print('2. Emprestar um livro')
            print('3. Devolver um livro')
            print('4. Sair do programa')

            try:
                opcao = int(input('Digite uma das opções: '))
            except ValueError:
                print('Opção inválida. Por favor, escolha novamente.')
                continue

            if opcao == 1:
                biblioteca.adicionar_livro()
            elif opcao == 2:
                livro = input('Digite o nome do livro que deseja emprestar: ')
                biblioteca.emprestar_livro(livro)
            elif opcao == 3:
                livro = input('Digite o nome do livro que deseja devolver: ')
                biblioteca.devolver_livro(livro)
            elif opcao == 4:
                print('Saindo do programa. Até logo!')
                break
            else:
                print('Opção inválida. Por favor, escolha novamente.')

menu = Menu()
menu.menu()