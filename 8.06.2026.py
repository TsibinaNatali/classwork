# # айти наибольшее
# a = int(input("num"))
# b = int(input("num"))
# c = int(input("num"))
#
# if a > b and a > c:
#     print(a)
# elif b > c:
#     print(b)
# else:
#     print(c)
# #яв-ся ли четным
# num = int(input("number"))
# if num % 2 == 0:
#     print("четное")
# else:
#     print("no")
# #  сть ли в числе 3
# ab = int(input("двухзначное"))
# b = ab % 10 or ab // 10
# if b == 3:
#     print(f"es {b}")
# elif a == 3:
#     print(f"es {a}")
# else:
#     print("no")
#
#  # попадет ли число в диапазон
#
# n = int(input())
# print(10<=n<=20)
#
#
# a1 = int(input("1num"))
# b1 = int(input("2num"))
# print(a1 % 3 == 0 and b1 % 3 == 0)



# h=int(input("num"))
# while h >= 0:
#     print(h, end=" ")
#     h = h-1

# k = int(input("num"))
# a=0
# while a <= k:
#     print(a, end=" ")
#     a = a+1

# a=int(input("num1"))
# b=int(input("num1"))
# if a>b:
#     a,b = b,a
# while a<=b :
#
#     print(a, end=" ")
#     a=a+1
#
#
# a1=int(input("num1"))
# b1=int(input("num1"))
# if a1<b1:
#     a1,b1 = b1,a1
# while a1>=b1 :
#     print(a1, end=" ")
#     a1=a1-1

# a = 0
# while a<=10
#     print(a)
#     a+= 2

# h= int(input())
# l= int(input())
# if h>l:  h,l = l,h
# if h%2: h+=1
# while h<=l:
#      # if h%2==0:
#      print(h)
#         # h+=1
#      h += 2
# 1 вариант
# a = int(input("num"))
# n=0
# while n<=a:
# if n% 10==3:
#     print(n)
#     n+=1
# # второй вариант
# a = int(input("num"))
# n = 3
# while n <= a:
#     print(n)
#     n += 10
# a = int(input("num"))


n = int(input("сколько чисел"))
s=0
while n>0:
    n-=1
    num=int(input("введите число"))
    s+=num
    n-=1
    print(s)