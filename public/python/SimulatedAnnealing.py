import numpy as np
from copy import deepcopy
from random import randint
from random import shuffle
from random import random
from random import sample
from readXls import ReadData, SingleSolution

class SimulatedAnnealing:
    def __init__(self, clean_data, min_temp, max_temp, cooling_rate=0.9996):
        self.clean_data = clean_data
        self.data = deepcopy(clean_data)
        #self.original = deepcopy(grade)
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.cooling_rate = cooling_rate
        self.actual_state = SingleSolution(data)
        self.best_state = self.actual_state
        self.next_state = None

    def run(self):
        self.actual_state.generate_solution()
        temp = self.max_temp
        counter = 0

        while temp > self.min_temp and self.best_state.fitness() != 0:
            counter += 1

            if counter % 100 == 0:
                # print('---------------------------------------------------------------------------')
                # print('---------------------------------------------------------------------------')
                # print('---------------------------------------------------------------------------')
                # print('---------------------------------------------------------------------------')
                print('Iteracao #%s - quantidade de conflitos: %s' % (counter, self.best_state.fitness()))
                #
                # for fase in self.best_state.grade:
                #     for index, dia in enumerate(fase):
                #         for slot in dia:
                #             if (slot is None):
                #                 print("(-)")
                #             else:
                #                 print(slot.nome_disciplina + " " + slot.professor.nome_chave)

            #new_state = self.actual_state
            new_data = deepcopy(clean_data)
            new_state = SingleSolution(new_data)
            new_state.generate_solution()

            actual_energy = self.actual_state.fitness()
            new_energy = new_state.fitness()

            if random() < self.accept_prob(actual_energy, new_energy, temp):
                self.actual_state = new_state

            if self.actual_state.fitness() < self.best_state.fitness():
                self.best_state = self.actual_state

            temp = temp * self.cooling_rate

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


        print('Solucao: \n%s' % self.best_state)
        print('conflitos: ' + str(self.best_state.fitness()))

    # swapa dias discilpna de lugar aleatoriamente
    # def generate_next_state(self, actual_state):
    #     new_state = SingleSolution(data)
    #     new_state.generate_solution()
    #     return new_state

    @staticmethod
    def accept_prob(actual_energy, next_energy, temp):
        if next_energy < actual_energy:
            return 1

        #return 0
        return np.exp((actual_energy - next_energy) / temp)

if __name__ == '__main__':
    data = ReadData()
    data.read_professores()
    data.read_disciplinas()
    clean_data = deepcopy(data)
    algorithm = SimulatedAnnealing(clean_data, 1, 100)
    algorithm.run()

    # for index, dia in enumerate(matriz):
    #    for slot in dia:
    #        if(slot is None):
    #            print("(-)")
    #        else:
    #         print(slot.nome_disciplina + " " +slot.professor.nome_chave)
    #    print("------------------------------------------------------------------------")
