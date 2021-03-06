# Дан список L и число n. Сформируйте и верните новый список, 
# содержащий номера позиций, на которых n находится в списке L
# reveals all places of the entered number in the list

# Список и число на вход
example_list = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 67, 1, 2, 3, 4, 5, 6, 7, 7, 1]
exaple_number = 1

# Распечатка списка с индексами для проверки решения
for i in range(len(example_list)):
    print('element ', example_list[i], 'has ', i, ' index')

# Функция возвращает список всех индексов данного числа в данном списке    
def eduse_all_indexes_of_given_number(given_number, given_list):
    new_list  = [] # список индексов
    to_save_list = []
    to_save_list.extend(given_list) # место для хранения первоначального списка
    #to_save_list = given_list 
    displacement = 0 # при удалении элемента из списка нумерация смещается - этот костыль помогает это учесть
    for i in given_list:
        if i == given_number:
            new_list.append(given_list.index(given_number) + displacement) # добавляю в новый список индекс с учетом смещения
            given_list.remove(given_number) # удаляю посчитанный элемент, если не сделать индекс всегда будет одинаковый так как возвращает индекс первого встреченного элемента
            displacement += 1 # после удаление индексы съехали на 1
    given_list.clear()
    given_list.extend(to_save_list) # пытаюсь восстановить список !!! и нифига не выходит!!!
    return new_list 

# каша из принтов для просмотра результатов функции 
# Печатаю первоначальное число
print('\nexaple_number = ', exaple_number)

# Печатаем лист с индексами числа 1 в изначальном списке
print('\nlist of indexes of {}:\n'.format(exaple_number), eduse_all_indexes_of_given_number(exaple_number, example_list), sep='')

# применение функции и запись её результата в новый список
list_of_index_given_number = eduse_all_indexes_of_given_number(exaple_number, example_list)

# печать первоночального листа после использования функции 
# Должен быть неизменным, но это не так
print('\nlist after function, but before removing elements by list of indexes (it should content: "1"):\n', example_list, sep='')

# удаляем из списка элементы по возвращенным индексам. 
# Должны быть удалены все 1, если бы мы шли по неизмененному первоначальному списку
displacement2 = 0
for i in list_of_index_given_number:
    example_list.remove(example_list[i - displacement2])
    displacement2 += 1
# мне не ясно, если функция меняет исходный список, 
# почему после прохождения по этому циклу список не становится короче 
# Ведь на 0, 6, 12, 20 местах находятся другие числа. 
# Чего он их не удаляет?

# Печатаю первоначальный лист
print('\nlist after function, and after removing elements by list of indexes:\n', example_list, sep='')