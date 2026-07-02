marks = [2,3,-4,3,8,-9,9,0,-4]
# for i in range(len(marks)):
#     if i < 0:
#         print(i, end="")
#
# for i in range(len(marks)):
#     if marks[i] < 0:
#         i *= -1
#         print(i, end="")
# for i in range(len(marks)//2):
#     marks[i],marks[len(marks)-(i+1)] =marks[len(marks)-(i+1)],marks[i]
#     print(i, end="")

# name = ["вася","петя","оля","света"]
# flag=True
# for i in range(1,len(name)):
#     if len(name[i]) != len(name[0]):
#         flag=False
#         break
# print(flag and "все равны" or "разные")
# for i in name:
#     if i[len(name[i])-1] == "a":
#         print(i, end="")

numbers = [[2,5,8,9],
           [3,6,2,7]]
for i in range(len(numbers)):
    summ = 0
    for j in numbers[i]:
        summ += j
        print(j,end="\t")
    print("|",summ)
print("----------------")
result = 0

# for i in range(len(numbers[0])):
#     summ = 0
#     for j in range(len(numbers)):
#         summ += numbers[j][i]
#     print("|",summ,end="\t")
#     result += summ
# print("|",result)






