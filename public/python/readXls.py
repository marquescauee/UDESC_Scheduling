from copy import deepcopy
from random import shuffle

import os
import sys

import pandas as pd
import numpy as np

from constraints import ConstraintHard, ConstraintSoft, DiasNaoMinistradasHard, DiasNaoMinistradasSoft, \
    DeveSerNoiteCheiaHard, DeveSerNoiteCheiaSoft
from professor import Professor
from disciplina import Disciplina


class ReadData:
    def __init__(self):
        self.cacheProfessores = {}
        self.disciplinas = []
        self.primeiraFase = []
        self.segundaFase = []
        self.terceiraFase = []
        self.quartaFase = []
        self.quintaFase = []
        self.sextaFase = []
        self.setimaFase = []
        self.oitavaFase = []

    def read_professores(self):
        df = pd.read_excel(os.getcwd()+ "/python/planilhas/" + sys.argv[1], header=None, usecols=[0,1,3,5,6])
        df = df.replace(np.nan, None)
        # Pega os dados com um dicionario
        data = df.to_dict(orient='records')

        # Pega o cabecalho na primeira linha
        header = data[0]
        data = data[1:]  # Ignorando a linha do cabecalho para os dados

        # Remove as colunas sem info do cabecalho.
        header = [coluna for coluna in header if pd.notna(coluna)]

        professores = []

        i = 1
        for linha in data:
            hard = DiasNaoMinistradasHard(False, linha[3])
            soft = DiasNaoMinistradasSoft(False, linha[5], linha[6])
            professor = Professor(i, linha[0], linha[1], hard, soft)
            self.cacheProfessores[linha[0]] = professor
            professores.append(professor)
            i += 1

        return professores

    # print(cacheProfessores)

    # for p in professores:
    #     print(p.nome_chave + ' ' + p.nome_completo + ' ' + str(p.diasNaoMinistradosHard.getDiasNaoMinistradas()) + ' ' + str(p.diasNaoMinistradosSoft.getDiasNaoMinistradas()))

    #####################################################################

    def read_disciplinas(self):

        df = pd.read_excel(os.getcwd()+ "/python/planilhas/" + sys.argv[2], header=None, usecols=[0,1,2,3,4,6,7,9,10,11,12])
        df = df.replace(np.nan, None)

        data = df.to_dict(orient='records')

        header = data[0]

        data = data[1:]

        header = [coluna for coluna in header if pd.notna(coluna)]

        i = 1
        for linha in data:
            hard_constraints = [DiasNaoMinistradasHard(False, linha[6]), DeveSerNoiteCheiaHard(False, linha[7])]
            soft_constraints = [DiasNaoMinistradasSoft(False, linha[9], linha[10]),
                                DeveSerNoiteCheiaSoft(False, linha[11], linha[12])]
            disciplina = Disciplina(i, self.cacheProfessores[linha[0]], linha[1], linha[2], linha[3], linha[4],
                                    hard_constraints,
                                    soft_constraints)  ## como la em cima ta setado as cols aqui tem q fazer tbm, bem meme

            ##ADICIONA CONSTRAINT DA DSISCIPLNA NO PRFOESSOR QUE LECIONA
            prof = self.cacheProfessores[linha[0]]
            prof.addHardConstraints(hard_constraints)

            if (disciplina.fase == '1'):
                self.primeiraFase.append(disciplina)
            if (disciplina.fase == '2'):
                self.segundaFase.append(disciplina)
            if (disciplina.fase == '3'):
                self.terceiraFase.append(disciplina)
            if (disciplina.fase == '4'):
                self.quartaFase.append(disciplina)
            if (disciplina.fase == '5'):
                self.quintaFase.append(disciplina)
            if (disciplina.fase == '6'):
                self.sextaFase.append(disciplina)
            if (disciplina.fase == '7'):
                self.setimaFase.append(disciplina)
            if (disciplina.fase == '8'):
                self.oitavaFase.append(disciplina)

            self.disciplinas.append(disciplina)
            i += 1


# for disciplina in primeiraFase:
#     print(f'ID: {disciplina.id}, ' \
#                        f'Nome-Chave Professor: {disciplina.professor}, ' \
#                        f'Fase da Disciplina: {disciplina.fase}, ' \
#                        f'Código da Disciplina: {disciplina.codigo_disciplina}, ' \
#                        f'Nome da Disciplina: {disciplina.nome_disciplina}, ' \
#                        f'Créditos da Disciplina: {disciplina.creditos_disciplina}, ' \
#                        f'Aula Sábado: {disciplina.aula_sabado}, ' \
#                        f'Hard 1: {disciplina.hard_constraints[0].getDiasNaoMinistradas()}, ' \
#                        f'Hard 2: {disciplina.hard_constraints[1].getDeveSerNoiteCheia()}, ' \
#                        f'Soft 1: {disciplina.soft_constraints[0].getDiasNaoMinistradas()}, ' \
#                        f'Peso 1: {disciplina.soft_constraints[0].getPeso()}, ' \
#                        f'Soft 2: {disciplina.soft_constraints[1].getDeveSerNoiteCheia()}, ' \
#                        f'Peso 2: {disciplina.soft_constraints[1].getPeso()}')
#     print("----------------------------------------------------------------")

# ESSA FUNCAO NAO ADICIONA DICIPLINAS QUE VIOALM RESTRICOES
def gerarSolucaoParical(matriz, disciplinas):
    podeSabado = []
    for indice, disciplina in enumerate(disciplinas):
        if disciplina.aula_sabado == 'S':
            disciplinas.pop(indice)
            podeSabado.append(disciplina)

    for indice, disciplina in enumerate(disciplinas):
        i = 0
        j = 0
        qntdAulas = int(disciplina.creditos_disciplina / 2)
        alocadas = 0
        while not disciplina.alocada:
            if i == 5:
                break
            if matriz[i][j] is None and disciplina.professor.horariosAlocados[i][j] is None:
                matriz[i][j] = disciplina
                alocadas += 1
                disciplina.professor.horariosAlocados[i][j] = disciplina
                if qntdAulas == alocadas:
                    disciplina.alocada = True
            j += 1
            if j == 2:  # Avance para a próxima coluna
                j = 0
                i += 1  # Avance para a próxima linha
            if i == 6:  # Verifique se todas as linhas foram preenchidas
                break

    for index, disciplina in enumerate(podeSabado):
        i = 0
        j = 0
        qntdAulas = int(disciplina.creditos_disciplina / 2)
        alocadas = 0
        while not disciplina.alocada:
            if matriz[i][j] is None and disciplina.professor.horariosAlocados[i][j] is None:
                matriz[i][j] = disciplina
                alocadas += 1
                disciplina.professor.horariosAlocados[i][j] = disciplina
                if qntdAulas == alocadas:
                    disciplina.alocada = True
            j += 1
            if j == 2:  # Avance para a próxima coluna
                j = 0
                i += 1  # Avance para a próxima linha
            if i == 6:  # Verifique se todas as linhas foram preenchidas
                break

    conflitos = 0;
    for index, dia in enumerate(matriz):
        for slot in dia:
            if (slot is None):
                if index != 5:
                    conflitos += 1
                print("(-)")
            else:
                print(slot.nome_disciplina + " " + slot.professor.nome_chave)
        print("------------------------------------------------------------------------")

    return conflitos


# ESSA FUNCAO GERA A GRADE POR COMPLETO, ADICIONANDO AS DISCIPLINAS QUE VIOLAM RESTRICOES
def gerar(matriz, disciplinas):
    #np.random.shuffle(disciplinas)

    podeSabado = []

    disciplinasNaoAlocadas = []

    disciplinasNaoAlocadasSabado = []

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
                disciplina.professor.horariosAlocados[i][j] = disciplina
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

    conflitos = 0;
    for index, disciplina in enumerate(disciplinasNaoAlocadas):
        i = 0
        j = 0
        qntdAulas = int(disciplina.creditos_disciplina / 2)
        alocadas = 0
        while not disciplina.alocada:
            if matriz[i][j] is None:
                matriz[i][j] = disciplina
                alocadas += 1
                disciplina.nome_disciplina = disciplina.nome_disciplina + " *********"
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
                disciplina.professor.horariosAlocados[i][j] = disciplina
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


    for index, disciplina in enumerate(disciplinasNaoAlocadasSabado):
        i = 0
        j = 0
        qntdAulas = int(disciplina.creditos_disciplina / 2)
        alocadas = 0
        while not disciplina.alocada:
            if matriz[i][j] is None:
                matriz[i][j] = disciplina
                alocadas += 1
                disciplina.nome_disciplina = disciplina.nome_disciplina + " *********"
                conflitos += 1
                if qntdAulas == alocadas:
                    disciplina.alocada = True
            j += 1
            if j == 2:  # Avance para a próxima coluna
                j = 0
                i += 1  # Avance para a próxima linha
            if i == 5:  # Verifique se todas as linhas foram preenchidas
                break

    return conflitos




#
# totalConflitos = 0;
#
# print("--------------------------------------------------------------------")
# print("PRIMEIRA FASE:")
# matriz1Fase = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]
#
# conf1= gerar(matriz1Fase, primeiraFase)
# totalConflitos += conf1
# print ("NUMERO DE CONFLITOS:" + str(conf1))
#
# print("--------------------------------------------------------------------")
# print("SEGUNDA FASE:")
# matriz2Fase = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]
#
# conf2 = gerar(matriz2Fase, segundaFase)
# totalConflitos += conf2
# print ("NUMERO DE CONFLITOS:" + str(conf2))
#
# print("--------------------------------------------------------------------")
# print("TERCEIRA FASE:")
# matriz3Fase = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]
#
# conf3=gerar(matriz3Fase, terceiraFase)
# totalConflitos += conf3
# print ("NUMERO DE CONFLITOS:" + str(conf3))
#
#
# print("--------------------------------------------------------------------")
# print("QUARTA FASE:")
# matriz4Fase = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]
#
# conf4 = gerar(matriz4Fase, quartaFase)
# totalConflitos += conf4
# print ("NUMERO DE CONFLITOS:" + str(conf4))
#
# print("--------------------------------------------------------------------")
# print("QUINTA FASE:")
# matriz5Fase = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]
#
# conf5 = gerar(matriz5Fase, quintaFase)
# totalConflitos += conf5
# print ("NUMERO DE CONFLITOS:" + str(conf5))
#
#
# print("--------------------------------------------------------------------")
# print("SEXTA FASE:")
# matriz6Fase = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]
#
# conf6 = gerar(matriz6Fase, sextaFase)
# totalConflitos =+ conf6
# print ("NUMERO DE CONFLITOS:" + str(conf6))
#
#
# print("--------------------------------------------------------------------")
# print("SETIMA FASE:")
# matriz7Fase = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]
#
# conf7 = gerar(matriz7Fase, setimaFase)
# totalConflitos += conf7
# print ("NUMERO DE CONFLITOS:" + str(conf7))
#
# print("--------------------------------------------------------------------")
# print("OITAVA FASE:")
# matriz8Fase = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]
#
# conf8 = gerar(matriz8Fase, oitavaFase)
# totalConflitos += conf8
# print ("NUMERO DE CONFLITOS:" + str(conf8))
#
# print("TOTAL DE CONFLITOS DA GRADE:" + str(totalConflitos))

class SingleSolution:
    def __init__(self, original_data):
        self.grade = None
        self.totalConflitos = None
        self.data = deepcopy(original_data)

    def generate_solution(self):
        self.totalConflitos = 0

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
                self.totalConflitos += gerar(matriz1Fase, self.data.primeiraFase)
            elif fase == 2:
                shuffle(self.data.segundaFase)
                self.totalConflitos += gerar(matriz2Fase, self.data.segundaFase)
            elif fase == 3:
                shuffle(self.data.terceiraFase)
                self.totalConflitos += gerar(matriz3Fase, self.data.terceiraFase)
            elif fase == 4:
                shuffle(self.data.quartaFase)
                self.totalConflitos += gerar(matriz4Fase, self.data.quartaFase)
            elif fase == 5:
                shuffle(self.data.quintaFase)
                self.totalConflitos += gerar(matriz5Fase, self.data.quintaFase)
            elif fase == 6:
                shuffle(self.data.sextaFase)
                self.totalConflitos += gerar(matriz6Fase, self.data.sextaFase)
            elif fase == 7:
                shuffle(self.data.setimaFase)
                self.totalConflitos += gerar(matriz7Fase, self.data.setimaFase)
            elif fase == 8:
                shuffle(self.data.oitavaFase)
                self.totalConflitos += gerar(matriz8Fase, self.data.oitavaFase)

        self.grade = [matriz1Fase, matriz2Fase, matriz3Fase, matriz4Fase,
                      matriz5Fase, matriz6Fase, matriz7Fase,matriz8Fase]  # grade de todas as fasese em ordem

    def fitness(self):
        return self.totalConflitos

    def mutate(self):
        self.generate_solution()