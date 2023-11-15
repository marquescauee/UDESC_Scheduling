from copy import deepcopy
from random import shuffle

import pandas as pd
import numpy as np

import os
import sys

from constraints import ConstraintHard, ConstraintSoft, DiasNaoMinistradasHard, DiasNaoMinistradasSoft, \
    DeveSerNoiteCheiaHard, DeveSerNoiteCheiaSoft
from professor import Professor
from disciplina import Disciplina


class ReadData:
    def __init__(self):
        self.cacheProfessores = {}
        self.professores = []
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
        try:
            #df = pd.read_excel("planilhas/professores.xls", header=None, usecols=[0, 1, 3, 5, 6])
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
                self.professores.append(professor)
                professores.append(professor)
                i += 1

            return professores
        except:
            print("ERRO DE PLANILHA")
            sys.exit(1)

    def read_disciplinas(self):
        try:
            #df = pd.read_excel("planilhas/disciplinas.xls", header=None, usecols=[0, 1, 2, 3, 4, 6, 7, 9, 10, 11, 12])
            df = pd.read_excel(os.getcwd()+ "/python/planilhas/" + sys.argv[2], header=None, usecols=[0,1,2,3,4,6,7,9,10,11,12]) ##descobrir uma mehlor forma de nao pegar as coisas vazias
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
        except:
            print("ERRO DE PLANILHA")
            sys.exit(1)
