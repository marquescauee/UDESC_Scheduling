import numpy as np
from copy import deepcopy
from random import randint
from random import shuffle
from random import random
from random import sample
from readXls import ReadData, SingleSolutionSofts
import pandas as pd
import time
import os

class SimulatedAnnealing:
    def __init__(self, clean_data, min_temp, max_temp, cooling_rate=0.9998):
        self.clean_data = clean_data
        self.data = deepcopy(clean_data)
        #self.original = deepcopy(grade)
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.cooling_rate = cooling_rate
        self.actual_state = SingleSolutionSofts(data)
        self.best_state = self.actual_state
        self.next_state = None

    def run(self):
        self.actual_state.generate_solution()
        temp = self.max_temp
        counter = 0

        start_time = time.time()
        while temp > self.min_temp:
            counter += 1

            if(self.best_state.softFitness() == 0 and self.best_state.fitness() == 0):
                break

            if counter % 100 == 0:
                print('Iteracao #%s - Conflitos: %s | Softs: %s' % (counter, self.best_state.fitness(), self.best_state.softFitness()))

            #new_state = self.actual_state
            new_data = deepcopy(clean_data)
            new_state = SingleSolutionSofts(new_data)
            new_state.generate_solution()

            actual_energy = self.actual_state.fitness()
            actual_soft_energy = self.actual_state.softFitness()
            new_energy = new_state.fitness()
            new_soft_energy = new_state.softFitness()


            if random() < self.accept_prob(actual_energy, new_energy, actual_soft_energy, new_soft_energy, temp):
                self.actual_state = new_state

            if (self.actual_state.fitness() < self.best_state.fitness() or
                (self.actual_state.fitness() == self.best_state.fitness() and self.actual_state.softFitness() < self.best_state.softFitness())):

                self.best_state = self.actual_state

            temp = temp * self.cooling_rate

        end_time = time.time()

        for fase in self.best_state.grade:
            i = 0
            for index, dia in enumerate(fase):
               i = 0
               for slot in dia:
                   if(slot is None):
                       print("(-)")
                   else:
                    print(slot.nome_disciplina + " " + slot.professor.nome_chave)
            print('\n')
            print('\n')
            print('|||||||||||||||||||||||||||||||||||||||||||')
            print('\n')
            print('\n')

        elapsed_time = end_time - start_time
        print('Solucao: \n%s' % self.best_state)
        print('conflitos: ' + str(self.best_state.fitness()))
        print('conflitos: ' + str(self.best_state.softFitness()))
        print('Tempo Decorrido: ' + str(elapsed_time))

        return self.best_state

    @staticmethod
    def accept_prob(actual_energy, next_energy, actual_soft_energy, next_soft_energy, temp):
        if next_energy < actual_energy or (next_energy == actual_energy and next_soft_energy < actual_soft_energy):
            return 1

        return np.exp((actual_energy - next_energy) / temp)

if __name__ == '__main__':
    data = ReadData()
    data.read_professores()
    data.read_disciplinas()
    clean_data = deepcopy(data)
    algorithm = SimulatedAnnealing(clean_data, 1, 100)
    solution = algorithm.run()

    dfs = []

    for fase in solution.grade:
        for dia in fase:
            if dia[0] is None:
                dia[0] = ' '
            else:
                dia[0] = dia[0].nome_disciplina

            if dia[1] is None:
                dia[1] = ' '
            else:
                dia[1] = dia[1].nome_disciplina

    dfs =[]
    pd.set_option('max_colwidth', None)

    for fase in solution.grade:
        df = pd.DataFrame({
             'Inicio - Final': ['18:50 - 19:40', '19:40 - 20:30', '20:40 - 21:30', '21:30 - 22:20'],
             'Segunda-Feira:': [fase[0][0], fase[0][0], fase[0][1], fase[0][1]],
             'Terça-Feira:': [fase[1][0], fase[1][0], fase[1][1], fase[1][1]],
             'Quarta-Feira:': [fase[2][0], fase[2][0], fase[2][1], fase[2][1]],
             'Quinta-Feira:': [fase[3][0], fase[3][0], fase[3][1], fase[3][1]],
             'Sexta-Feira:': [fase[4][0], fase[4][0], fase[4][1], fase[4][1]],
             'Sábado:': [fase[5][0], fase[5][0], fase[5][1], fase[5][1]],
        })

        dfs.append(df)

root_dir = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

writer = pd.ExcelWriter(root_dir + '/storage/app/public/solution/solucao.xlsx')

for index, df in enumerate(dfs):
    nomeSheet = 'Fase ' + str(index + 1)
    df.to_excel(writer, sheet_name = nomeSheet, index = False)

    for column in df:
        column_length = max(df[column].astype(str).map(len).max(), len(column))
        col_idx = df.columns.get_loc(column)
        writer.sheets[nomeSheet].set_column(col_idx, col_idx, column_length)

writer.close()

# df = pd.read_excel(root_dir + '/storage/app/public/solution/output.xlsx')
# df.to_excel(root_dir + '/storage/app/public/solution/output.xls')
