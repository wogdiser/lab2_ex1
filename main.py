# Lab 2
# Вариант 2.
# Zadanie 1.
# Заполните список случайными целыми числами.
# Найдите в списке все простые числа и скопируйте их в новый список.

import random

# ! does not check for natural numbers
def is_prime(num):
  if num > 1:
    for i in range(2, num):
      if (num % i) == 0:
        return False
        break
  return True

list = []
result_list = []

for i in range(6):
  list.append(random.randint(1, 20))

print(list)
print("check each element")

for j in range(len(list)):
  print(list[j])
  if is_prime(list[j]):
    result_list.append(list[j])
    print("saved:", list[j])

print(result_list)
