class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self):
        titulo = input('Digite o nome do livro: ')
        autor = input('Digite o autor do livro: ')
        try:
            for livro in self.livros:
                if livro.titulo == titulo:
                    print(f"O livro '{titulo}' já existe na biblioteca.")
                    return
            livro = Livro(titulo, autor)
            self.livros.append(livro)
            print(f"O título '{titulo}' de '{autor}' foi adicionado com sucesso.")
        except Exception as erro:
            print(f'Ocorreu um erro ao adicionar o livro: {erro.__class__}')

    def emprestar_livro(self, titulo):
        try:
            for livro in self.livros:
                if livro.titulo == titulo:
                    if livro.disponivel:
                        livro.disponivel = False
                        print(f"O livro '{titulo}' foi emprestado com sucesso.")
                        return livro
                    else:
                        print(f"O livro '{titulo}' não está disponível no momento. Tente novamente outro dia.")
                        return None
            print(f"O livro  '{titulo}' não foi encontrado.")
            return None
        except Exception as erro:
            print(f'Ocorreu um erro ao emprestar o livro: {erro.__class__}')
            return None

    def devolver_livro(self, titulo):
        try:
            for livro in self.livros:
                if livro.titulo == titulo:
                    if not livro.disponivel:
                        livro.disponivel = True
                        print(f"O livro '{titulo}' foi devolvido com sucesso.")
                        return livro
                    else:
                        print(f"O livro '{titulo}' já está disponível na biblioteca.")
                        return None
                elif livro.titulo != titulo:
                    print(f"O livro  '{titulo}' não foi encontrado.")
                    return None
        except Exception as erro:
            print(f'Ocorreu um erro ao devolver o livro: {erro.__class__}')
            return None