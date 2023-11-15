from constraints import DiasNaoMinistradasHard, DiasNaoMinistradasSoft


class Professor:
    def __init__(self, id, nome_chave, nome_completo, diasNaoMinistradosHard, diasNaoMinistradosSoft):
        self.id = id
        self.nome_chave = nome_chave
        self.nome_completo = nome_completo
        self.diasNaoMinistradosHard = diasNaoMinistradosHard
        self.diasNaoMinistradosSoft = diasNaoMinistradosSoft

        self.horariosAlocados = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]
        self.preferivelNaoDarAula = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]

        if(diasNaoMinistradosHard.getDiasNaoMinistradas() is not None):
            diasTexto = diasNaoMinistradosHard.getDiasNaoMinistradas().split(';')
            for dia in diasTexto:
                if dia == "SEG":
                    self.horariosAlocados[0][0] = "NAO PODE DAR AULA"
                    self.horariosAlocados[0][1] = "NAO PODE DAR AULA"

                if dia == "TER":
                    self.horariosAlocados[1][0] = "NAO PODE DAR AULA"
                    self.horariosAlocados[1][1] = "NAO PODE DAR AULA"

                if dia == "QUA":
                    self.horariosAlocados[2][0] = "NAO PODE DAR AULA"
                    self.horariosAlocados[2][1] = "NAO PODE DAR AULA"

                if dia == "QUI":
                    self.horariosAlocados[3][0] = "NAO PODE DAR AULA"
                    self.horariosAlocados[3][1] = "NAO PODE DAR AULA"

                if dia == "SEX":
                    self.horariosAlocados[4][0] = "NAO PODE DAR AULA"
                    self.horariosAlocados[4][1] = "NAO PODE DAR AULA"

                if dia == "SAB":
                    self.horariosAlocados[5][0] = "NAO PODE DAR AULA"
                    self.horariosAlocados[5][1] = "NAO PODE DAR AULA"

        if(diasNaoMinistradosSoft.getDiasNaoMinistradas() is not None):
            diasTexto = diasNaoMinistradosSoft.getDiasNaoMinistradas().split(';')
            for dia in diasTexto:
                if dia == "SEG":
                    self.preferivelNaoDarAula[0][0] = diasNaoMinistradosSoft.getPeso()
                    self.preferivelNaoDarAula[0][1] = diasNaoMinistradosSoft.getPeso()

                if dia == "TER":
                    self.preferivelNaoDarAula[1][0] = diasNaoMinistradosSoft.getPeso()
                    self.preferivelNaoDarAula[1][1] = diasNaoMinistradosSoft.getPeso()

                if dia == "QUA":
                    self.preferivelNaoDarAula[2][0] = diasNaoMinistradosSoft.getPeso()
                    self.preferivelNaoDarAula[2][1] = diasNaoMinistradosSoft.getPeso()

                if dia == "QUI":
                    self.preferivelNaoDarAula[3][0] = diasNaoMinistradosSoft.getPeso()
                    self.preferivelNaoDarAula[3][1] = diasNaoMinistradosSoft.getPeso()

                if dia == "SEX":
                    self.preferivelNaoDarAula[4][0] = diasNaoMinistradosSoft.getPeso()
                    self.preferivelNaoDarAula[4][1] = diasNaoMinistradosSoft.getPeso()

                if dia == "SAB":
                    self.preferivelNaoDarAula[5][0] = diasNaoMinistradosSoft.getPeso()
                    self.preferivelNaoDarAula[5][1] = diasNaoMinistradosSoft.getPeso()


    #ALOCA A DISCILINA NO HORARIO E RETORNA UMA VIOLACAO SOFT CASO SEJA PREFERIVEL NAO DAR AULA NAQUELA HORARIO
    def alocarHorario(self, i,j,disciplina):
        self.horariosAlocados[i][j] = disciplina
        if(self.preferivelNaoDarAula[i][j] is not None):
            disciplina.nome_disciplina = disciplina.nome_disciplina + "*"
            return 1 * self.preferivelNaoDarAula[i][j]
        return 0

    def addHardConstraints(self, hard_constraints):
        for hard_constraint in hard_constraints:
            if isinstance(hard_constraint, DiasNaoMinistradasHard):
                if(hard_constraint.getDiasNaoMinistradas() is not None):
                    diasTexto = hard_constraint.getDiasNaoMinistradas().split(';')
                    for dia in diasTexto:
                        if dia == "SEG":
                            self.horariosAlocados[0][0] = "NAO PODE DAR AULA"
                            self.horariosAlocados[0][1] = "NAO PODE DAR AULA"

                        if dia == "TER":
                            self.horariosAlocados[1][0] = "NAO PODE DAR AULA"
                            self.horariosAlocados[1][1] = "NAO PODE DAR AULA"

                        if dia == "QUA":
                            self.horariosAlocados[2][0] = "NAO PODE DAR AULA"
                            self.horariosAlocados[2][1] = "NAO PODE DAR AULA"

                        if dia == "QUI":
                            self.horariosAlocados[3][0] = "NAO PODE DAR AULA"
                            self.horariosAlocados[3][1] = "NAO PODE DAR AULA"

                        if dia == "SEX":
                            self.horariosAlocados[4][0] = "NAO PODE DAR AULA"
                            self.horariosAlocados[4][1] = "NAO PODE DAR AULA"

                        if dia == "SAB":
                            self.horariosAlocados[5][0] = "NAO PODE DAR AULA"
                            self.horariosAlocados[5][1] = "NAO PODE DAR AULA"

    def addSoftConstraints(self, soft_constraints):
        for soft_constraint in soft_constraints:
            if isinstance(soft_constraint, DiasNaoMinistradasSoft):
                if(soft_constraint.getDiasNaoMinistradas() is not None):
                    diasTexto = soft_constraint.getDiasNaoMinistradas().split(';')
                    for dia in diasTexto:
                        if dia == "SEG":
                            self.preferivelNaoDarAula[0][0] = "PREFERIVEL NAO DAR AULA"
                            self.preferivelNaoDarAula[0][1] = "PREFERIVEL NAO DAR AULA"

                        if dia == "TER":
                            self.preferivelNaoDarAula[1][0] = "PREFERIVEL NAO DAR AULA"
                            self.preferivelNaoDarAula[1][1] = "PREFERIVEL NAO DAR AULA"

                        if dia == "QUA":
                            self.preferivelNaoDarAula[2][0] = "PREFERIVEL NAO DAR AULA"
                            self.preferivelNaoDarAula[2][1] = "PREFERIVEL NAO DAR AULA"

                        if dia == "QUI":
                            self.preferivelNaoDarAula[3][0] = "PREFERIVEL NAO DAR AULA"
                            self.preferivelNaoDarAula[3][1] = "PREFERIVEL NAO DAR AULA"

                        if dia == "SEX":
                            self.preferivelNaoDarAula[4][0] = "PREFERIVEL NAO DAR AULA"
                            self.preferivelNaoDarAula[4][1] = "PREFERIVEL NAO DAR AULA"

                        if dia == "SAB":
                            self.preferivelNaoDarAula[5][0] = "PREFERIVEL NAO DAR AULA"
                            self.preferivelNaoDarAula[5][1] = "PREFERIVEL NAO DAR AULA"
