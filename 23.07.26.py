import random
# num1 = int(input("введите 1 число "))
# num2 = int(input("введите 2 число "))
# num3 = int(input("введите 3 число "))
# num4 = int(input("введите 4 число "))
# max=0
# if num1 > max:
#     max = num1
# if num2 > max:
#     max = num2
# if num3 > max:
#     max = num3
# if num4 > max:
#     max = num4
# print(max)


# 2
# a = int(input("введите 1 число "))
# b = int(input("введите последнее число "))
# if a < b:
#     a,b = b,a
# for i in range(a,b-1,-1):
#     print(i)

# 3
# n = int(input("введите сторону квадрата "))
# surent_number = 5
# for i in range(n):
#     for j in range(n):
#         print(surent_number, end="\t")
#         surent_number +=1
#     print()
# 4
# simvol = input("введите символ ")
# if simvol.isupper():
#     print(f"{simvol} является ")
# else:
#     print("нет")
# 5
my_list = [0,0,0,0,0,0,0,0]
for i in range(0,len(my_list),3):
    my_list[i] = random.randint(0,99)
    print(my_list[i])
# 6
# rows = 4
# cols = 4
a = int(input("введите начало диапазона "))
end = int(input("введите конец диапазона "))
if a > end:
    a, end = end, a
mas = [[0,0,0,0,0,
        0,0,0,0,0]]
for i in range(len(mas)):
    for j in range(mas):


