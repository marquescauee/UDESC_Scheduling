from constraints import DeveSerNoiteCheiaHard, DeveSerNoiteCheiaSoft


class Disciplina:
    def __init__(self, id, professor, codigo_disciplina, nome_disciplina,creditos_disciplina, aula_sabado, hard_constraints, soft_constraints):
        self.id = id
        self.nome_disciplina = nome_disciplina
        self.codigo_disciplina = codigo_disciplina
        self.creditos_disciplina = creditos_disciplina
        self.professor = professor
        self.aula_sabado = aula_sabado
        self.soft_constraints = soft_constraints
        self.hard_constraints = hard_constraints

        self.fase = codigo_disciplina[0]
        self.alocada = False
        self.deveSerNoiteCheia = None
        self.preferivelSerNoiteCheia = None
        self.pesoNoiteCheia = None

        for hard in hard_constraints:
            if isinstance(hard, DeveSerNoiteCheiaHard):
                if (hard.getDeveSerNoiteCheia() ==  'S'):
                    self.deveSerNoiteCheia ='S'
                elif (hard.getDeveSerNoiteCheia() ==  'N'):
                    self.deveSerNoiteCheia = 'N'
                else:
                    self.deveSerNoiteCheia = None

        for soft in soft_constraints:
            if isinstance(soft, DeveSerNoiteCheiaSoft):
                if (soft.getDeveSerNoiteCheia() ==  'S'):
                    self.preferivelSerNoiteCheia ='S'
                    self.pesoNoiteCheia = soft.getPeso()
                elif (soft.getDeveSerNoiteCheia() ==  'N'):
                    self.preferivelSerNoiteCheia = 'N'
                    self.pesoNoiteCheia = soft.getPeso()
                else:
                    self.preferivelSerNoiteCheia = None
                    self.pesoNoiteCheia = None


    def add_hard_constraint(self, constraint):
        self.hard_constraints.append(constraint)

    def add_soft_constraint(self, constraint):
        self.soft_constraints.append(constraint)
