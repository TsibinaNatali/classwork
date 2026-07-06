# #
# # def min_index(numbers):
# #     index = 0
# #     min_valie = numbers[0]
# #     for i in range(len(numbers)):
# #         if min_valie > numbers[i]:
# #              min_valie = numbers[i]
# #              index = i
# #     return index
# # numbers = [2,5,8,9,0]
# # print(min_index(numbers))
# #
# # a = int(input())
# # b = int(input())
# # if a>b: a,b = b,a
# #
# # list = [2,4]
# # if list[0] > list[1]:
# #     list[0],list[1] = list[1],list[0]
# # print(list)
# # -------------------------пузырьковая сортиравка
def swap(list,index1,index2):
    list[index1],list[index2] = list[index2],list[index1]
#
# list = [2,1,4,3,8,13,2,5]
# for j in range(len(list)-1):
#     for i in range(len(list)-1-j):
#         if list[i] > list[i+1]:
#             swap(list,i,i+1)
# print(list)
#
# list = [2,1,4,3,8,13,2,5]
# for j in range(len(list)-1):
#     for i in range(len(list)-1-j):
#         if list[i] > list[i+1]:
#             swap(list,i,i+1)
#
# list = [2,1,4,3,8,13,2,5]
# count  = 0
# for j in range(len(list)-1):
#     flag = False
#     for i in range(len(list)-1-j):
#         count += 1
#         if list[i] > list[i+1]:
#             flag = True
#             swap(list,i,i+1)
#     if not flag:
#         break
# print(list)

# # сортировка вставкой
#  list=[2,1,4,5,3,4,67,2,6,2,7,4,3,5,2,6,7,3,67,6,43,7,34,65,34,6,3,5,3]
# count = 0
# for i in range(1,len(list)):
#     for j in range(i,0,-1):
#         count += 1
#         if list[j] < list[j-1]:
#             swap(list,j,j-1)
#         else:
#             break
# print(list,count)

def summa(s=0):
    num = int(input())
    s+=num
    if num == 0:
        return s
    else:
        return summa(s)
print(summa())


s=0
def summa():
    global s
    num = int(input())
    s+=num
    if num == 0:
        return s
    else:
        return summa()
print(summa())