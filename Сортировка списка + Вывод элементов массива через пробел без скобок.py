# Вводится N целых чисел (1<=N<=1000). Каждое число по модулю не больше 108. Выведите вначале отсортированные по возрастанию неотрицательные, потом отсортированные по возрастанию модуля отрицательные.
# Внимание: не забудьте подумать про ноль
# Формат входных данных
# Целое число N - количество чисел. Далее N целых чисел, каждое с новой строчки.
# Формат выходных данных
# Отсортированные числа, в одну строку, через пробел.
N = int(input())
plus_numbers = []
minus_numbers = []
while N != 0:
    number = int(input())
    if number >= 0:
        plus_numbers.append(number)
        N = N - 1
    else:
        minus_numbers.append(number)
        N = N - 1
plus_numbers.sort()
minus_numbers.sort(reverse=True)
Answer = plus_numbers + minus_numbers
print(*Answer)



