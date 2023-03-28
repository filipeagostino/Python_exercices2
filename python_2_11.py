class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'

class Aluno(Pessoas):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.nome = nome
        self.idade = idade
        self.curso = curso
    
    def __str__(self):
        return f'Aluno -> {super().__str__()} (Curso: {self.curso})'

class Professor(Pessoas):
    def __init__(self, nome, idade, turma):
        super().__init__(nome, idade)
        self.nome = nome
        self.idade = idade
        self.turma = turma
    
    def __str__(self):
        return f'Professor -> {super().__str__()} (Turma: {self.turma})'

pessoa1 = Pessoas('Orleide', 97)
a = Aluno('André', 20, 'Economia')

print(isinstance(pessoa1, Pessoas), isinstance(pessoa1, Professor), isinstance(pessoa1, Aluno))
print(isinstance(a, Pessoas), isinstance(a, Professor), isinstance(a, Aluno))
