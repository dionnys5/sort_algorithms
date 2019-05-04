import psutil
import time


class Sort:
    def __init__(self, lista):
        self.lista = lista
        self.total_troca = 0
        self.total_comparacoes = 0
        self.cpu = 0
        self.memory = 0
        self.time_exec = None

    def BubbleOne(self):
        start = time.time()
        L = len(self.lista)
        for j in range(L):
            for i in range(L-1):
                self.total_comparacoes += 1
                if self.lista[i] > self.lista[i+1]:
                    self.total_troca += 1
                    aux = self.lista[i]
                    self.lista[i] = self.lista[i+1]
                    self.lista[i+1] = aux
        self.memory = psutil.virtual_memory().used
        self.cpu = psutil.cpu_percent()
        self.time_exec = time.time() - start

    def BubbleTwo(self):
        start = time.time()
        L = len(self.lista)
        for j in range(L):
            for i in range(L-1, j, -1):
                self.total_comparacoes += 1
                if self.lista[i] < self.lista[i - 1]:
                    self.total_troca += 1
                    aux = self.lista[i]
                    self.lista[i] = self.lista[i - 1]
                    self.lista[i - 1] = aux
        self.memory = psutil.virtual_memory().used
        self.cpu = psutil.cpu_percent()
        self.time_exec = time.time() - start

    def BubbleThree(self):
        start = time.time()
        j = 1
        troca = True
        L = len(self.lista)
        while(j<= L and troca):
            troca = False
            for i in range(L-1):
                self.total_comparacoes += 1
                if self.lista[i] > self.lista[i+1]:
                    self.total_troca += 1
                    troca = True
                    aux = self.lista[i]
                    self.lista[i] = self.lista[i+1]
                    self.lista[i+1] = aux
        self.memory = psutil.virtual_memory().used
        self.cpu = psutil.cpu_percent()
        self.time_exec = time.time() - start

    def InsertionSort(self):
        start = time.time()
        L = len(self.lista)
        for i in range(L):
            eleito = self.lista[i]
            j = i - 1
            self.total_comparacoes += 1
            while j >= 1 and (self.lista[j] > eleito):
                self.lista[j+1] = self.lista[j]
                self.total_troca += 1
                j = j - 1
            self.lista[j+1] = eleito
        self.memory = psutil.virtual_memory().used
        self.cpu = psutil.cpu_percent()
        self.time_exec = time.time() - start

    def SelectionSort(self):
        start = time.time()
        L = len(self.lista)
        for i in range(L-1):
            eleito = self.lista[i]
            menor = self.lista[i+1]
            pos = i + 1
            for j in range(i, L, 1):
                self.total_comparacoes += 1
                if self.lista[j] < menor:
                    self.total_troca += 1
                    menor = self.lista[j]
                    pos = j
            if menor < eleito:
                self.total_troca += 1
                self.lista[i] = self.lista[pos]
                self.lista[pos] = eleito
        self.memory = psutil.virtual_memory().used
        self.cpu = psutil.cpu_percent()
        self.time_exec = time.time() - start
