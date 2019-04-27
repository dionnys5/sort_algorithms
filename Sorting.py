class Sort:
    def __init__(self, lista):
        self.lista = lista

    def BubbleOne(self):
        L = len(self.lista)
        for j in range(L):
            for i in range(L-1):
                if self.lista[i] > self.lista[i+1]:
                    aux = self.lista[i]
                    self.lista[i] = self.lista[i+1]
                    self.lista[i+1] = aux

    def BubbleTwo(self):
        L = len(self.lista)
        for j in range(L):
            for i in range(L-1, j, -1):
                if self.lista[i] < self.lista[i - 1]:
                    aux = self.lista[i]
                    self.lista[i] = self.lista[i - 1]
                    self.lista[i - 1] = aux

    def BubbleThree(self):
        j = 1
        troca = True
        L = len(self.lista)
        while(j<= L and troca):
            troca = False
            for i in range(L-1):
                if self.lista[i] > self.lista[i+1]:
                    troca = True
                    aux = self.lista[i]
                    self.lista[i] = self.lista[i+1]
                    self.lista[i+1] = aux

    def InsertionSort(self):
        L = len(self.lista)
        for i in range(L):
            eleito = self.lista[i]
            j = i - 1
            while j >= 1 and (self.lista[j] > eleito):
                self.lista[j+1] = self.lista[j]
                j = j - 1
            self.lista[j+1] = eleito

    def SelectionSort(self):
        L = len(self.lista)
        for i in range(L-1):
            eleito = self.lista[i]
            menor = self.lista[i+1]
            pos = i + 1
            for j in range(i, L, 1):
                if self.lista[j] < menor:
                    menor = self.lista[j]
                    pos = j
            if menor < eleito:
                self.lista[i] = self.lista[pos]
                self.lista[pos] = eleito

'''
1 para 𝑖 ← 1 até |𝐿| − 1 faça
2 𝑒𝑙𝑒𝑖𝑡𝑜 ← 𝐿𝑖
3 𝑚𝑒𝑛𝑜𝑟 ← 𝐿𝑖+1
4 𝑝𝑜𝑠 ← 𝑖 + 1
5 para 𝑗 ← 𝑖 + 1 até |𝐿| faça
6 se 𝐿𝑗 < 𝑚𝑒𝑛𝑜𝑟 então
7 𝑚𝑒𝑛𝑜𝑟 ← 𝐿𝑗
8 𝑝𝑜𝑠 ← 𝑗
9 fim
10 fim
11 se 𝑚𝑒𝑛𝑜𝑟 < 𝑒𝑙𝑒𝑖𝑡𝑜 então
12 𝐿𝑖 ← 𝐿𝑝𝑜𝑠
13 𝐿𝑝𝑜𝑠 ← 𝑒𝑙𝑒𝑖𝑡𝑜
14 fim
15 fim
'''
