from constraints import DiasNaoMinistradasHard


class Professor:
    def __init__(self, id, nome_chave, nome_completo, diasNaoMinistradosHard, diasNaoMinistradosSoft):
        self.horariosAlocados = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]

        self.id = id
        self.nome_chave = nome_chave
        self.nome_completo = nome_completo
        if(diasNaoMinistradosHard.getDiasNaoMinistradas() is not None):
            diasTexto = diasNaoMinistradosHard.getDiasNaoMinistradas().split(';')
            for dia in diasTexto:
                if dia == "SEG":
                    self.horariosAlocados[0][0] = "NAO PODE DAR AULA"
                    self.horariosAlocados[0][1] = "NAO PODE DAR AULA"
                    # diasNumero.append([0], [0])
                    # diasNumero.append([0], [1])
                if dia == "TER":
                    self.horariosAlocados[1][0] = "NAO PODE DAR AULA"
                    self.horariosAlocados[1][1] = "NAO PODE DAR AULA"
                    # diasNumero.append([1], [0])
                    # diasNumero.append([1], [1])
                if dia == "QUA":
                    self.horariosAlocados[2][0] = "NAO PODE DAR AULA"
                    self.horariosAlocados[2][1] = "NAO PODE DAR AULA"
                    # diasNumero.append([2], [0])
                    # diasNumero.append([2], [1])
                if dia == "QUI":
                    self.horariosAlocados[3][0] = "NAO PODE DAR AULA"
                    self.horariosAlocados[3][1] = "NAO PODE DAR AULA"
                    # diasNumero.append([3], [0])
                    # diasNumero.append([3], [1])
                if dia == "SEX":
                    self.horariosAlocados[4][0] = "NAO PODE DAR AULA"
                    self.horariosAlocados[4][1] = "NAO PODE DAR AULA"
                    # diasNumero.append([4], [0])
                    # diasNumero.append([4], [1])
                if dia == "SAB":
                    self.horariosAlocados[5][0] = "NAO PODE DAR AULA"
                    self.horariosAlocados[5][1] = "NAO PODE DAR AULA"
                    # diasNumero.append([5], [0])
                    # diasNumero.append([5], [1])

        self.diasNaoMinistradosHard = diasNaoMinistradosHard
        self.diasNaoMinistradosSoft = diasNaoMinistradosSoft

    def addHardConstraints(self, hard_constraints):
        for hard_constraint in hard_constraints:
            if isinstance(hard_constraint, DiasNaoMinistradasHard):
                if(hard_constraint.getDiasNaoMinistradas() is not None):
                    diasTexto = hard_constraint.getDiasNaoMinistradas().split(';')
                    for dia in diasTexto:
                        if dia == "SEG":
                            self.horariosAlocados[0][0] = "NAO PODE DAR AULA"
                            self.horariosAlocados[0][1] = "NAO PODE DAR AULA"
                            # diasNumero.append([0], [0])
                            # diasNumero.append([0], [1])
                        if dia == "TER":
                            self.horariosAlocados[1][0] = "NAO PODE DAR AULA"
                            self.horariosAlocados[1][1] = "NAO PODE DAR AULA"
                            # diasNumero.append([1], [0])
                            # diasNumero.append([1], [1])
                        if dia == "QUA":
                            self.horariosAlocados[2][0] = "NAO PODE DAR AULA"
                            self.horariosAlocados[2][1] = "NAO PODE DAR AULA"
                            # diasNumero.append([2], [0])
                            # diasNumero.append([2], [1])
                        if dia == "QUI":
                            self.horariosAlocados[3][0] = "NAO PODE DAR AULA"
                            self.horariosAlocados[3][1] = "NAO PODE DAR AULA"
                            # diasNumero.append([3], [0])
                            # diasNumero.append([3], [1])
                        if dia == "SEX":
                            self.horariosAlocados[4][0] = "NAO PODE DAR AULA"
                            self.horariosAlocados[4][1] = "NAO PODE DAR AULA"
                            # diasNumero.append([4], [0])
                            # diasNumero.append([4], [1])
                        if dia == "SAB":
                            self.horariosAlocados[5][0] = "NAO PODE DAR AULA"
                            self.horariosAlocados[5][1] = "NAO PODE DAR AULA"
                            # diasNumero.append([5], [0])
                            # diasNumero.append([5], [1])