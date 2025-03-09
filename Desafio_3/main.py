from agenda_telefonica import Agenda

class Menu():
    def menu(self):

        agenda = Agenda()

        while True:
            print('\nMenu de Usuário:')
            print('1. Adicionar um novo contato')
            print('2. Remover um contato existente')
            print('3. Buscar um contato pelo nome')
            print('4. Atualizar informações de um contato')
            print('5. Listar todos os contatos na agenda')
            print('6. Sair do programa')

            opcao = input('Escolha uma das opções do menu: ')

            if opcao == '1':
                agenda.adicionar_contato()
            elif opcao == '2':
                nome = input('Digite o nome do contato a ser removido: ')
                agenda.deletar_contato(nome)
            elif opcao == '3':
                nome = input('Digite o nome do contato a ser buscado: ')
                contato = agenda.buscar_contato(nome)
                if contato:
                    print(f"Contato encontrado: Nome: '{contato.nome}', Telefone: '{contato.telefone}'")
                else:
                    print('Contato não encontrado.')
            elif opcao == '4':
                nome = input('Digite o nome do contato a ser atualizado: ')
                agenda.atualizar_contato(nome)
            elif opcao == '5':
                agenda.listar_contatos()
            elif opcao == '6':
                print('Saindo do programa. Até logo!')
                break
            else:
                print('Opção inválida. Por favor, escolha novamente.')
menu = Menu()
menu.menu()