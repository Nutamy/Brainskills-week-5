example_list = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 67, 1, 2, 3, 4, 5, 6, 7, 7, 1]
exaple_number = 1

i = 0
indexes = []

for item in example_list:
  if exaple_number == item:
    indexes.append(i)
  i+=1

print(indexes)