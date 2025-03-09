class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self):
        nome = input('Digite o nome do contato: ')
        telefone = input('Digite o telefone do contato: ')

        for contato in self.contatos:
            if contato.nome == nome:
                escolha = input(f"O contato '{nome}' já existe. Deseja atualizar? (s/n): ").strip().lower()
                if escolha == 's':
                    self.atualizar_contato(nome)
                    return  # Evita duplicação do contato
                else:
                    print(f"Contato '{nome}' não foi alterado.")
                return

        novo_contato = Contato(nome, telefone)
        self.contatos.append(novo_contato)
        print(f"Contato '{nome}' adicionado com sucesso.")

    def atualizar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                novo_nome = input(
                    f"Digite o novo nome para '{nome}' (ou pressione Enter para manter o mesmo): ").strip()
                novo_telefone = input(
                    f"Digite o novo telefone para '{nome}' (ou pressione Enter para manter o mesmo): ").strip()

                if novo_nome:
                    contato.nome = novo_nome
                if novo_telefone:
                    contato.telefone = novo_telefone

                print(f"Contato atualizado com sucesso: Nome: '{contato.nome}', Telefone: '{contato.telefone}'")
                return
        print("Contato não encontrado.")

    def deletar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                print(f"Contato '{nome}' removido com sucesso.")
                return
        print("Contato não encontrado.")

    def listar_contatos(self):
        if not self.contatos:
            print("Nenhum contato na agenda.")
            return
        for contato in self.contatos:
            print(f"Nome: '{contato.nome}', Telefone: '{contato.telefone}'")

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
        return None