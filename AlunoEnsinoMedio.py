from Aluno import Aluno

class AlunoEM(Aluno):

    def __init__(self,cod = None, nome = None, matricula=None, ano = None)
        super().__init__(cod,nome,matricula)
            self.ano = ano
    
    def imprimir ()