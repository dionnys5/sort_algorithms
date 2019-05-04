from Sorting import Sort

with open('100000.csv', 'r') as lista:
    lista = lista.read().split('\n')
    print('lista unordered: ', lista)

lista_int = [int(x) for x in lista]
sorter = Sort(lista_int)
# sorter.BubbleOne()
sorter.BubbleTwo()
# sorter.BubbleThree()
# sorter.SelectionSort()
# sorter.InsertionSort()

with open('relatorio_bubbleTwo100000.txt', 'w', encoding='UTF8') as file:
    file.write('Total troca: ' + str(sorter.total_troca) + '\n')
    file.write('Total comparações: ' + str(sorter.total_comparacoes) + '\n')
    file.write('Total CPU: ' + str(sorter.cpu) + '\n')
    file.write('Total memoria: ' + str(sorter.memory) + '\n')
    file.write('Total Tempo: ' + str(sorter.time_exec))
print('\n\n')
print(sorter.lista)
