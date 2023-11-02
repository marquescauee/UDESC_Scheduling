class Disciplina:
    def __init__(self, id, professor, codigo_disciplina, nome_disciplina,
                 creditos_disciplina, aula_sabado, hard_constraints, soft_constraints):
        self.id = id
        self.professor = professor
        self.fase = codigo_disciplina[0]
        self.codigo_disciplina = codigo_disciplina
        self.nome_disciplina = nome_disciplina
        self.creditos_disciplina = creditos_disciplina
        self.aula_sabado = aula_sabado
        self.hard_constraints = hard_constraints
        self.soft_constraints = soft_constraints
        self.alocada = False
    
    def add_hard_constraint(self, constraint):
        self.hard_constraints.append(constraint)
        
    def add_soft_constraint(self, constraint):
        self.soft_constraints.append(constraint)
