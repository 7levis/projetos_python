class Aluno :
    def __init__ (self, nome):
        self.nome = nome
        self.notas = []
    
    def adicionar_nota (self, nota):
        self.nota.append(nota)

    def calcular_media(self):
        if sum(self.notas) / len(self.notas)

class Turma:
    def __init__(self):
        self.alunos = []

    def adcionar_aluno(self, aluno):
        self.aluno.append(aluno)

    def calcular_media_turma(self):
        total_media = sum(aluno.calcular_media() for aluno in self.alunos)
        if len (self.alunos) == 0:
            return 0
        return total_media / len(self.alunos)
  
turma = Turma()

aluno1 = Aluno("Maria")
aluno1.adicionar_nota(9.0)
aluno1.adicionar_nota(8.0)

aluno2 = Aluno("João")
aluno2.adicionar_nota(7.5)
aluno2.adicionar_nota(6.5)

aluno3 = Aluno("Ana")
aluno3.adicionar_nota(9.0)
aluno3.adicionar_nota(9.0)

turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)
turma.adicionar_aluno(aluno3)

for aluno in turma.alunos:
    print(f"Aluno: {aluno.nome}, Media: {aluno.calcular_media()}")

print (f"Média geral da turma: {turma.calcular_media_turma()}")
       
