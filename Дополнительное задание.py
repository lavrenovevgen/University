import statistics # чтобы функция statistics работала она была импортирована

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = sorted(list(students)) # создаем новый список предварительно преобразовав множество students в список с помощью list(students)
average_score = [] # Создаем пока пустой список со средним баллом
for grades1 in grades: # функция for поможет перебрать список с оценками каждого ученика
    average_score.append(float(statistics.mean(grades1))) # функция statistics.mean посчитает средний бал каждого ученика
    # функция append добавит по порядку средний бал каждого ученика в новый список  average_score
students_average_score = dict(zip(students_list, average_score))
print(students_average_score)