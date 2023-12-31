from copy import deepcopy
from random import shuffle

class SingleSolution:
    def __init__(self, original_data):
        self.grade = None
        self.totalConflitos = None
        self.totalConflitosSoft = None
        self.data = deepcopy(original_data)

    def generate_solution(self):
        self.totalConflitos = 0
        self.totalConflitosSoft = 0

        fases = [1, 2, 3, 4, 5, 6, 7, 8]

        shuffle(fases)

        matriz1Fase = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]

        matriz2Fase = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]

        matriz3Fase = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]

        matriz4Fase = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]

        matriz5Fase = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]

        matriz6Fase = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]

        matriz7Fase = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]

        matriz8Fase = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]

        # Loop para gerar as matrizes de acordo com a ordem aleatória.
        for fase in fases:
            if fase == 1:
                shuffle(self.data.primeiraFase)
                conflito, softConflito = gerarComSoft(matriz1Fase, self.data.primeiraFase)
                self.totalConflitos += conflito
                self.totalConflitosSoft += softConflito
            elif fase == 2:
                shuffle(self.data.segundaFase)
                conflito, softConflito = gerarComSoft(matriz2Fase, self.data.segundaFase)
                self.totalConflitos += conflito
                self.totalConflitosSoft += softConflito
            elif fase == 3:
                shuffle(self.data.terceiraFase)
                conflito, softConflito = gerarComSoft(matriz3Fase, self.data.terceiraFase)
                self.totalConflitos += conflito
                self.totalConflitosSoft += softConflito
            elif fase == 4:
                shuffle(self.data.quartaFase)
                conflito, softConflito = gerarComSoft(matriz4Fase, self.data.quartaFase)
                self.totalConflitos += conflito
                self.totalConflitosSoft += softConflito
            elif fase == 5:
                shuffle(self.data.quintaFase)
                conflito, softConflito = gerarComSoft(matriz5Fase, self.data.quintaFase)
                self.totalConflitos += conflito
                self.totalConflitosSoft += softConflito
            elif fase == 6:
                shuffle(self.data.sextaFase)
                conflito, softConflito = gerarComSoft(matriz6Fase, self.data.sextaFase)
                self.totalConflitos += conflito
                self.totalConflitosSoft += softConflito
            elif fase == 7:
                shuffle(self.data.setimaFase)
                conflito, softConflito = gerarComSoft(matriz7Fase, self.data.setimaFase)
                self.totalConflitos += conflito
                self.totalConflitosSoft += softConflito
            elif fase == 8:
                shuffle(self.data.oitavaFase)
                conflito, softConflito = gerarComSoft(matriz8Fase, self.data.oitavaFase)
                self.totalConflitos += conflito
                self.totalConflitosSoft += softConflito

        self.grade = [matriz1Fase, matriz2Fase, matriz3Fase, matriz4Fase,
                      matriz5Fase, matriz6Fase, matriz7Fase, matriz8Fase]  # grade de todas as fasese em ordem

    def fitness(self):
        return self.totalConflitos

    def softFitness(self):
        return self.totalConflitosSoft;

    def mutate(self):
        self.generate_solution()


def gerarComSoft(matriz, disciplinas):
    podeSabado = []

    disciplinasNaoAlocadas = []

    disciplinasNaoAlocadasSabado = []

    conflitos_soft = 0;

    for indice, disciplina in enumerate(disciplinas):
        if disciplina.aula_sabado == 'S':
            disciplinas.pop(indice)
            podeSabado.append(disciplina)

    for indice, disciplina in enumerate(disciplinas):
        i = 0
        j = 0
        qntdAulas = int(disciplina.creditos_disciplina / 2)
        alocadas = 0
        alocados = []
        while not disciplina.alocada:
            if matriz[i][j] is None and disciplina.professor.horariosAlocados[i][j] is None:
                matriz[i][j] = disciplina
                alocados.append([i, j])
                alocadas += 1
                conflitos_soft += disciplina.professor.alocarHorario(i, j, disciplina)
                if qntdAulas == alocadas:
                    disciplina.alocada = True
            j += 1
            if j == 2:  # Avance para a próxima coluna
                j = 0
                i += 1  # Avance para a próxima linha
            if i == 5:
                if disciplina.alocada is False:
                    for ij in alocados:
                        matriz[ij[0]][1] = None
                    disciplinasNaoAlocadas.append(disciplina)
                break

    # ADICIONA AS DISCIPLINAS DE SEG - SEX QUE CAUSAM CONFLITO E INCREMENTA O CONTADOR DE CONFLITOS
    conflitos = 0

    for index, disciplina in enumerate(disciplinasNaoAlocadas):
        i = 0
        j = 0
        qntdAulas = int(disciplina.creditos_disciplina / 2)
        alocadas = 0
        while not disciplina.alocada:
            if matriz[i][j] is None:
                matriz[i][j] = disciplina
                alocadas += 1
                disciplina.nome_disciplina = disciplina.nome_disciplina + '!!!!!!'
                conflitos += 1
                if qntdAulas == alocadas:
                    disciplina.alocada = True
            j += 1
            if j == 2:  # Avance para a próxima coluna
                j = 0
                i += 1  # Avance para a próxima linha
            if i == 5:  # Verifique se todas as linhas foram preenchidas
                break

    for index, disciplina in enumerate(podeSabado):
        i = 0
        j = 0
        qntdAulas = int(disciplina.creditos_disciplina / 2)
        alocadas = 0
        alocados = []
        while not disciplina.alocada:
            if matriz[i][j] is None and disciplina.professor.horariosAlocados[i][j] is None:
                matriz[i][j] = disciplina
                alocados.append([i, j])
                alocadas += 1
                conflitos_soft += disciplina.professor.alocarHorario(i, j, disciplina)
                if qntdAulas == alocadas:
                    disciplina.alocada = True
            j += 1
            if j == 2:  # Avance para a próxima coluna
                j = 0
                i += 1  # Avance para a próxima linha
            if i == 6:  # Verifique se todas as linhas foram preenchidas
                if disciplina.alocada is False:
                    for ij in alocados:
                        matriz[ij[0]][1] = None
                    disciplinasNaoAlocadasSabado.append(disciplina)
                break

    # ADICIONA AS DISCIPLINAS DE SABADO QUE CAUSAM CONFLITO E INCREMENTA O CONTADOR DE CONFLITOS
    for index, disciplina in enumerate(disciplinasNaoAlocadasSabado):
        i = 0
        j = 0
        qntdAulas = int(disciplina.creditos_disciplina / 2)
        alocadas = 0
        while not disciplina.alocada:
            if matriz[i][j] is None:
                matriz[i][j] = disciplina
                alocadas += 1
                disciplina.nome_disciplina = disciplina.nome_disciplina + '!!!!!!'
                conflitos += 1
                if qntdAulas == alocadas:
                    disciplina.alocada = True
            j += 1
            if j == 2:  # Avance para a próxima coluna
                j = 0
                i += 1  # Avance para a próxima linha
            if i == 5:  # Verifique se todas as linhas foram preenchidas
                break

    # CONTABILIZA AS VIOLACOES DE DEVE SER NOITE CHEIA
    for index, dia in enumerate(matriz):
        if dia[0] and dia[1] is not None:
            if dia[0] == dia[1]:
                if dia[0].deveSerNoiteCheia == 'N' or dia[1].deveSerNoiteCheia == 'N':
                    if dia[0].deveSerNoiteCheia == 'N':
                        conflitos += 1
                        dia[0].nome_disciplina = dia[0].nome_disciplina + "!!!"

                    if dia[1].deveSerNoiteCheia == 'N':
                        conflitos += 1
                        dia[1].nome_disciplina = dia[1].nome_disciplina + "!!!"


            else:
                if dia[0].deveSerNoiteCheia == 'S' or dia[1].deveSerNoiteCheia == 'S':
                    if dia[0].deveSerNoiteCheia == 'S' :
                        conflitos += 1
                        dia[0].nome_disciplina = dia[0].nome_disciplina + "!!!"
                    if dia[1].deveSerNoiteCheia == 'S':
                        conflitos += 1
                        dia[1].nome_disciplina = dia[1].nome_disciplina + "!!!"

            if dia[0] != dia[1]:
                if ((dia[0].creditos_disciplina / 2) % 2 == 1 and dia[0].deveSerNoiteCheia == 'S') or (
                    (dia[1].creditos_disciplina / 2) % 2 == 1 and dia[1].deveSerNoiteCheia == 'S'):
                    for isDiaCheio in matriz:
                        if isDiaCheio[0] == dia[0] and isDiaCheio[1] == dia[0]:
                            conflitos -= 1
                            dia[0].nome_disciplina = str(dia[0].nome_disciplina).replace('!', '')
                            break
                        elif isDiaCheio[0] == dia[1] and isDiaCheio[1] == dia[1]:
                            conflitos -= 1
                            dia[1].nome_disciplina = str(dia[1].nome_disciplina).replace('!', '');
                            break

        elif dia[0] is None and dia[1] is not None:
            if dia[1].deveSerNoiteCheia == 'S':
                conflitos += 1
                dia[1].nome_disciplina = dia[1].nome_disciplina + "!!!"
        elif dia[0] is not None and dia[1] is None:
            if dia[0].deveSerNoiteCheia == 'S':
                dia[0].nome_disciplina = dia[0].nome_disciplina + "!!!"
                conflitos += 1

    # SOFT NOITE CHEIA
    for index, dia in enumerate(matriz):
        if dia[0] and dia[1] is not None:
            if dia[0] == dia[1]:
                if dia[0].preferivelSerNoiteCheia == 'N' or dia[1].preferivelSerNoiteCheia == 'N':
                    if dia[0].pesoNoiteCheia is not None:
                        conflitos_soft += 1 * dia[0].pesoNoiteCheia
                        dia[0].nome_disciplina = dia[0].nome_disciplina + "*"

                    if dia[1].pesoNoiteCheia is not  None:
                        conflitos_soft += 1 * dia[1].pesoNoiteCheia
                        dia[1].nome_disciplina = dia[1].nome_disciplina + "*"
                    # if dia[0].preferivelSerNoiteCheia == 'N' and dia[1].preferivelSerNoiteCheia == 'N':
                    #     conflitos_soft += 1

            else:
                if dia[0].preferivelSerNoiteCheia == 'S' or dia[1].preferivelSerNoiteCheia == 'S':
                    if dia[0].pesoNoiteCheia is not None:
                        conflitos_soft += 1 * dia[0].pesoNoiteCheia
                        dia[0].nome_disciplina = dia[0].nome_disciplina + "*"
                    if dia[1].pesoNoiteCheia is not None:
                        conflitos_soft += 1 * dia[1].pesoNoiteCheia
                        dia[1].nome_disciplina = dia[1].nome_disciplina + "*"
                    # if dia[0].preferivelSerNoiteCheia == 'S' and dia[1].preferivelSerNoiteCheia == 'S':
                    #     conflitos_soft += 1

            if dia[0] != dia[1]:
                if ((dia[0].creditos_disciplina / 2) % 2 == 1 and dia[0].preferivelSerNoiteCheia == 'S') or (
                    (dia[1].creditos_disciplina / 2) % 2 == 1 and dia[1].preferivelSerNoiteCheia == 'S'):
                    for isDiaCheio in matriz:
                        if isDiaCheio[0] == dia[0] and isDiaCheio[1] == dia[0] and dia[0].preferivelSerNoiteCheia == 'S':
                            conflitos_soft -= 1 * dia[0].pesoNoiteCheia
                            dia[0].nome_disciplina = str(dia[0].nome_disciplina).replace('*', '');
                            break
                        elif isDiaCheio[0] == dia[1] and isDiaCheio[1] == dia[1] and dia[1].preferivelSerNoiteCheia == 'S':
                            conflitos_soft -= 1 * dia[1].pesoNoiteCheia
                            dia[1].nome_disciplina = str(dia[1].nome_disciplina).replace('*', '');
                            break

        elif dia[0] is None and dia[1] is not None:
            if dia[1].preferivelSerNoiteCheia == 'S':
                conflitos_soft += 1 * dia[1].pesoNoiteCheia
                dia[1].nome_disciplina = dia[1].nome_disciplina + "*"
        elif dia[0] is not None and dia[1] is None:
            if dia[0].preferivelSerNoiteCheia == 'S':
                conflitos_soft += 1 * dia[0].pesoNoiteCheia
                dia[0].nome_disciplina = dia[0].nome_disciplina + "*"

    return conflitos, conflitos_soft
