import random
# a = int(input("начало "))
# b = int(input("конец "))
# matrix = [0,0,0,0,0,0,0,0,0,0,]
# for i in range(len(matrix)):
#     matrix[i] = random.randint(1,99)
#     print(matrix[i],end=" ""\t")
# max = matrix[0]
# max_index = 0
# # for i in matrix:
# #     if i > max:
# #         max = matrix[i]
# # print(max)
#
# for i in range(len(matrix)):
#     if matrix[i] > max:
#         max = matrix[i]
#         max_index = i
# print(max)

# matrix_2 = [2,5,7,8,13,25,3,12,6,8,9]
# n=0
# for i in range(len(matrix)):
#     if matrix_2[i] % 2 == 0 :
#         matrix_2[n]= matrix[i]
#         n+=1
# for i in range(len(matrix)):
#     if matrix_2[i] % 2 != 0:
#         matrix_2[n] = matrix[i]
#         n += 1
# print(matrix)
# print(matrix_2)
# ---------------------------функции------------------
# def show_list():
#     print()
#     for i in list_1:
#         for j in i:
#             print(j, end="/t")
#             print
# list_1 = [[23,5,3,5,2,5,3,6]
#           [23,5,39,5,2,58,3,6]
#           [23,5,34,5,2,54,3,6]]

def start_programm():
    print(f"начало программы ")


start_programm()
print("№1")
start_programm()
print("№2")
start_programm()
print("№3")

def maximym(list_1):
    max = list_1[0]
    for i in range(len(list_1)):
        if list_1[i] > max:
            max = list_1[i]
    return max
numbe = [23,5,3,5,2,5,3,6]
maximym(numbe)

def generate_random_list(list_1):
    for i in range(len(list_1)):
        list_1[i]= random.randint(1,99)

generate_random_list(numbe)

# def aver(a,b,c,d):
#     return(a+b+c+d)/4

def aver(list):
    summ=0
    for i in list:
        summ += i
    return summ/len(list)
def sr_ball(list_2):
    for i in range()

school= [[2,3,5,7,8,4,5,6,3]
         [2,4,5,3]
         [2,5,4,4,5,5,]]
def sr_ball(school):
    summ = 0
    for i in range(school):
        summ += aver(i)
    print(summ/len(list))

def scool_user(list):
    max = 0
    for i in range(len(school)):
        if max<maximum(school[i]):
            max=maximum(school[i])
            index_max = i

