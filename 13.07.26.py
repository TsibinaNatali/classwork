import random
# st =input("ввод")
# print(st.count(" ")+1)
# spisoc = []
# s = int(input(" ввод "))
# for i in range(s):
#     spisoc.append(random.randint(1,9))
#
# print(spisoc)

# def rem(list1,num):
#     while num in list1:
#         list1.remove(num)
#
#     return list1
#
# def pop_list(ls,a):
#     i=0
#     size = len(ls)
#     while i < size:
#         if i == a:
#             ls.pop(a)
#             size -= 1
#             i -= 1
#         i += 1
#     return ls
#
# list1 = [2,4,6,8,3,6,3,8,3]
# print(rem(list1,3))
# print(pop_list(list1,3))
students = []
students_marks = []
while True:
    var = int(input("1- добавить, 2 - удалить, 3 - вывести"))
    if var ==1:
        name = input(" введите имя ")
        students.append(name)
        students_marks.append([])
    elif var == 2:
        index = int(input("введите номер студента "))
        if 1 <= index <= len(students):
            students.pop(index-1)
            students_marks.pop(index-1)
        else:
            print("такого нет")
    elif var==3:
        for i in range(len(students)):
            print(f"{i+1}. {students[i]} : { students_marks[i]}")







