# a = int(input("a"))
# b = int(input("b"))
# s=0
# for i in range(a, b+1, 1):
#     s=+i
# print(s)
#
#
# c = int(input("c"))
# if c<0:
#     for i in range(0, c-1, -1):
#         print(i)
# else:
#     for i in range(c,-1, 1):
#         print(i)
#
# f = int(input("f"))
# fs=0
# for i in range(1, f+1, 1):
#     fs*=i
# print(fs)
#
# max = int(input("c"))
# for i in range(4):
#     c=int(input())
#     if c > max:
#         print(c)
# sum=0
# j=0
# for i in range(1,5):
#     j=int(input("j"))
#     j %= 10
# if i == 3:
#     sum +=j
#  print(sum)

# column = int(input("n"))
# row = int(input("n"))
# for i in range(row):
#     print("*"*column)


# column = int(input("n"))
# row = int(input("n"))
# for i in range(row):
#     for j in range(column):
#         print("*",end="")
#     print()

# k=0
# column = int(input("n"))
# row = int(input("n"))
# for i in range(row):
#     for j in range(column):
#         print(k,end="")
#         k+=1
#     print(i)

# k=0
# column = int(input("n"))
# row = int(input("n"))
# for i in range(1,row+1):
#     for j in range(1,column+1):
#         print(f"{i}:{j}",end=" ")
#     print()

# n = int(input("n"))
# for i in range(n):
#     print("* "* (i+1))
#
# n = int(input("n"))
# for i in range(n):
#     print("* "* (n-i))
#
# n = int(input("n"))
# for i in range(n):
#     print("  *"*(n+1))
#
# n = int(input("n"))
# for i in range(1,n+1):
#     print("  "*(n-i)+"* "*(i))
#
# n = int(input("n"))
# for i in range(n, 1, -1):
#     print("  "*(n-i)+"* "*(i))

# n = int(input("n"))
# for i in range(n):
#     print((n-i)+" *"*(i)*" *")


# n = int(input("n"))
# print("* "*(n))
# for i in range(n-2):
#     print("* "+ "  " *(n-2) + "*")
# print("* "*n)


n = int(input("n"))
for i in range((n+1)//2):
    print(" "*i + "* "*(n-i*2))

