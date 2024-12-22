immutable_va = 'Курс: Python, всего задач:', 12, 'затрачено часов:', 1.5, True, [False,'Anton',1,3.4]
print(immutable_va)
#immutable_va[1] = 13 Так как объект "кортеж" не поддерживает назначение элементов их изменить нельзя
mutable_list = ['Курс: Python, всего задач:', 12, 'затрачено часов:', 1.5, True, [False,'Anton',1,3.4]]
mutable_list[0] = 'Решено задач: '
print(mutable_list)