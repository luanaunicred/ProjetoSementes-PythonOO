from agenda_telefonica import Contato, AgendaTelefonica

class Menu:
    def __init__(self):
        self.agenda = AgendaTelefonica()

    def exibir_menu(self):
        while True:
            print('\n--- Menu de Usuário ---')
            print('1. Adicionar um novo contato')
            print('2. Remover um contato existente')
            print('3. Buscar um contato pelo nome')
            print('4. Atualizar informações de um contato')
            print('5. Listar todos os contatos na agenda')
            print('6. Sair do programa')

            opcao = input('Escolha uma das opções do menu: ').strip()

            if opcao == '1':
                self.adicionar_contato()
            elif opcao == '2':
                self.remover_contato()
            elif opcao == '3':
                self.buscar_contato()
            elif opcao == '4':
                self.atualizar_contato()
            elif opcao == '5':
                self.listar_contatos()
            elif opcao == '6':
                print('Saindo do programa. Até logo!')
                break
            else:
                print('Opção inválida. Por favor, tente novamente.')

    def adicionar_contato(self):
        nome = input('Digite o nome do contato: ').strip()
        telefone = input('Digite o telefone do contato: ').strip()
        contato = Contato(nome, telefone)
        if self.agenda.adicionarContato(contato):
            print(f"Contato '{nome}' adicionado com sucesso.")
        else:
            print(f"Contato com nome '{nome}' já existe na agenda.")

    def remover_contato(self):
        nome = input('Digite o nome do contato a ser removido: ').strip()
        if self.agenda.removerContato(nome):
            print(f"Contato '{nome}' removido com sucesso.")
        else:
            print("Contato não encontrado.")

    def buscar_contato(self):
        nome = input('Digite o nome do contato a ser buscado: ').strip()
        contato = self.agenda.buscarContato(nome)
        if contato:
            print(f"Contato encontrado: Nome: '{contato.nome}', Telefone: '{contato.telefone}'")
        else:
            print("Contato não encontrado.")

    def atualizar_contato(self):
        nome = input('Digite o nome do contato a ser atualizado: ').strip()
        if not self.agenda.buscarContato(nome):
            print("Contato não encontrado.")
            return

        novo_nome = input('Digite o novo nome do contato: ').strip()
        novo_telefone = input('Digite o novo telefone do contato: ').strip()
        novo_contato = Contato(novo_nome, novo_telefone)

        if self.agenda.atualizarContato(nome, novo_contato):
            print(f"Contato '{nome}' atualizado com sucesso.")
        else:
            print("Erro ao atualizar o contato.")

    def listar_contatos(self):
        contatos = self.agenda.listarContatos()
        if not contatos:
            print("Agenda vazia.")
        else:
            for contato in contatos:
                print(f"Nome: '{contato.nome}', Telefone: '{contato.telefone}'")

# Ponto de entrada do programa
if __name__ == '__main__':
    menu = Menu()
    menu.exibir_menu()