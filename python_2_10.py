class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'

class Aluno(Pessoas):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso
    
    def __str__(self):
        return f'Aluno -> {super().__str__()} (Curso: {self.curso})'

class Professor(Pessoas):
    def __init__(self, nome, idade, turma):
        super().__init__(nome, idade)
        self.turma = turma
    
    def __str__(self):
        return f'Professor -> {super().__str__()} (Turma: {self.turma})'


pessoa = Pessoas('Cleiton', 25)
print(pessoa)
print('-=' * 30)
aluno = Aluno('Joãozinho', 11, 'Administração')
print(aluno)
print('-=' * 30)
professor = Professor('Marcos', 45, 'Adm')
print(professor)
