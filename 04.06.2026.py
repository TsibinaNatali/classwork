#
# a = int(input())
# b = int(input())
# c = int(input())
#
# if a > b:
#     if a > c:
#         print(a)
# if b > a:
#     if b > c:
#         print(b)
# if c > a:
#     if c > b:
#         print(c)
# else:
#     print("=")

num = int(input())
if num >= 0 or num <= 10:
    print("входит")
else:
    print("не входит")

num1 = int(input())
if num1 >= 0:
    if num1 <= 0:
        print("входит")
    else:
        print("не входит")

num2 = int(input())
if num2 > 0 & num2 == 0 and num2 < 10 & num2 == 10:
    print("входит")
else:
    print("не входит")



