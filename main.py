import random

n = random.randint(1, 100)

print("Угадай число от 1 до 100")

for i in range(3):
    x = int(input("Число: "))
    if x > n :
      print("меньше")
    if x < n :
        print("больше")
    if x == n:
        print("Угадал")
        break
    else:
        print("Не угадал")
print("Было:", n)


