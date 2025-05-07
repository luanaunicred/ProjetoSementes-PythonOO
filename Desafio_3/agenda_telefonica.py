from typing import List, Optional

class Contato:
    def __init__(self, nome: str, telefone: str):
        self.__nome = nome
        self.__telefone = telefone

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        self.__nome = novo_nome

    @property
    def telefone(self) -> str:
        return self.__telefone

    @telefone.setter
    def telefone(self, novo_telefone: str):
        self.__telefone = novo_telefone

class AgendaTelefonica:
    def __init__(self):
        self.contatos: List[Contato] = []

    def adicionarContato(self, contato: Contato) -> bool:
        if self.buscarContato(contato.nome):
            return False
        self.contatos.append(contato)
        return True

    def removerContato(self, nome: str) -> bool:
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                return True
        return False

    def buscarContato(self, nome: str) -> Optional[Contato]:
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
        return None

    def atualizarContato(self, nome: str, novoContato: Contato) -> bool:
        for i, contato in enumerate(self.contatos):
            if contato.nome == nome:
                self.contatos[i] = novoContato
                return True
        return False

    def listarContatos(self) -> List[Contato]:
        return self.contatos