# Дан список L и число n. Сформируйте и верните новый список, 
# содержащий номера позиций, на которых n находится в списке L
# reveals all places of the entered number in the list

example_list = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 67, 1, 2, 3, 4, 5, 6, 7, 7, 1]
exaple_number = 1
for i in range(len(example_list)):
    print('element ', example_list[i], 'has ', i, ' index')
def eduse_all_indexes_of_given_number(given_number, given_list):
    new_list  = []
    to_save_list =[]
    to_save_list = given_list
    displacement = 0
    for i in given_list:
        if i == given_number:
            new_list.append(given_list.index(given_number) + displacement)
            given_list.remove(given_number)
            displacement += 1
    given_list = to_save_list
    return new_list

print(eduse_all_indexes_of_given_number(exaple_number, example_list))
list_of_index_given_number = eduse_all_indexes_of_given_number(exaple_number, example_list)
print(example_list)
for i in list_of_index_given_number:
    example_list.remove(example_list[i])
print('exaple_number = ', exaple_number)
print(example_list)