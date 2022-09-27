#Магазин
#В магазине продаются разные коробки конфет, всего их N (1<=N<=1000). Для каждой известны P (цена) и K (сколько конфет внутри). У вас есть S денег. Нужно купить максимальное количество коробок. Вывести, сколько всего получится коробок, и сколько внутри окажется конфет.
#Формат входных данных
#Целое число N - количество коробок. Далее N строк, в каждой целое число P (цена) и целое число K (сколько конфет внутри). Далее на новой строке целое число S.
#Формат выходных данных
#Два целых числа через пробел - сколько купили коробок и сколько внутри в сумме конфет.
N = int(input())
list_prices = []
list_candies = []
while N != 0:
    price, candies = map(int, input().split())
    list_prices.append(price)
    list_candies.append(candies)
    N = N - 1
S = int(input())
boxes = 0
all_candies = 0
while S > 0:
    for index in range(0, len(list_prices)):
        if list_prices[index] == min(list_prices):
            S = S - list_prices[index]
            boxes += 1
            all_candies += list_candies[index]
            list_prices.pop(index)
            list_candies.pop(index)
            break
print(boxes, all_candies)