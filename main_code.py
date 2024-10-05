from random import randint
from time import perf_counter
def binary_search(data, elem):
    low = 0
    high = len(data) - 1

    while low <= high:

        middle = (low + high) // 2

        if data[middle] == elem:
            return middle
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1
    return -1

while True:
    numbers = [randint(0, 9) for _ in range(10)]
    numbers = set(numbers)
    numbers = list(numbers)
    numbers.sort()
    print(numbers)

    random_number = randint(0, len(numbers) - 1)
    print(random_number)

    try:
        try_ = int(input("Попробуйте угадать - какое из этих чисел я загадал? :"))
        tic = perf_counter()

        if binary_search(numbers, try_) == random_number:
            toc = perf_counter()
            print(f"Харош, угадал за {toc - tic:0.4f} секунд")

        else:
            print("Не угадал, лошара")

    except:
        print("Нормально введи, олень")
    next_ = input("Продолжить?")
    if next_ == "Нет":
        break
    elif next_ == "Да":
        continue
print("Работа программы завершена")
