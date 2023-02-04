from random import randint
from statistics import mean

# Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу.
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.

def zadacha1():
    # Так как не задано количество групп, определим его случайно - от 2 до 5
    qty_group = randint(2,5)
    print('Оценки за экзамен')
    max_avg_score = [0, 0]
    for i in range(1,qty_group+1):
        print(f'Группа {i}: ', end='')
        scores = [randint(2,5) for _ in range(randint(20,30))]
        print(scores, end='')
        print(f', Средний балл: {round(mean(scores),2)}')
        if mean(scores) > max_avg_score[1]:
            max_avg_score[0] = i
            max_avg_score[1] = mean(scores)
    print(f'У группы {max_avg_score[0]} наивысший средний балл за экзамен: {round(max_avg_score[1],2)}')

# Задача 2. Дана квадратная матрица, заполненная случайными числами. Определите, сумма элементов каких строк
# превосходит сумму главной диагонали матрицы.

def zadacha2():
    size = randint(2,10)
    print(f'Квадратная матрица размером {size}x{size}')
    diagonal = []
    row_sums = []
    for i in range(size):
        current_row = [randint(10,99) for _ in range(size)]
        diagonal.append(current_row[i])
        row_sums.append(sum(current_row))
        print(current_row)

    diagonal_sum = sum(diagonal)
    final_rows = []
    for i in range(0, len(row_sums)):
        if row_sums[i] > diagonal_sum:
            final_rows.append(i+1)

    if len(final_rows) > 0:
        print(f'Сумма элементов данных строк превышает сумму элементов главной диагонали: {final_rows}')
    else:
        print('Нет строк, сумма элементов которых превышает сумму элементов главной диагонали')

# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год.
# Каждому месяцу соответствует своя строка. Определите самый жаркий и самый холодный 7-дневный промежуток
# каждого месяца. Выведите их даты.

def zadacha3():
    month_days = [31, 30, 31, 31, 30]
    month_temps = [13, 19, 22, 22, 14]
    month_names = ['Май','Июнь','Июль','Август','Сентябрь']

    print('Средние дневные температуры с мая по сентябрь и самые холодные и жаркие 7-дневные промежутки для каждого месяца:\n')
    for i in range(0, len(month_days)):
        this_month_temps = [month_temps[i] + 0.1*randint(-40,40) for _ in range(month_days[i])]
        print(f'{month_names[i]}: {this_month_temps}')
        seven_days_min = [0,0,100]
        seven_days_max = [0,0,-100]
        for j in range(0, month_days[i]-6):
            if mean(this_month_temps[j:j+6]) < seven_days_min[2]:
                seven_days_min[0] = j
                seven_days_min[1] = j + 6
                seven_days_min[2] = mean(this_month_temps[j:j+6])
            if mean(this_month_temps[j:j+6]) > seven_days_max[2]:
                seven_days_max[0] = j
                seven_days_max[1] = j + 6
                seven_days_max[2] = mean(this_month_temps[j:j+6])
        print(f'Самый холодный 7-дневный промежуток для месяца {month_names[i]}: с {seven_days_min[0]+1} по {seven_days_min[1]+1} число. Средняя температура составила: {round(seven_days_min[2],1)}')
        print(f'Самый жаркий 7-дневный промежуток для месяца {month_names[i]}: с {seven_days_max[0]+1} по {seven_days_max[1]+1} число. Средняя температура составила: {round(seven_days_max[2],1)}')
        print()

print()
print('Задача 1')
print(zadacha1())
print()
print('Задача 2')
print(zadacha2())
print()
print('Задача 3')
print(zadacha3())