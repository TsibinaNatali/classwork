import random
# def create_random_set(size):
#     ls = []
#     while len(ls) < size:
#         num = random.randint(1, 9)
#         if num not in ls:
#             ls.append(num)
#             size -= 1
#     return ls
#
# s1 = set(create_random_set(6))
# print(s1)
# s2 = set(create_random_set(8))
# print(s2)
# print(len(s1.intersection(s2)))
# print((len(s1)+len(s2)-(len(s1.intersection(s2))*2) >len(s1.intersection(s2)) and "уникальных больше" or"бщих больше"))

# products= {
#     "name": "мышка",
#     "category": "продукты",
#     "price": 1200.50,
#     "count": 120,
#     "colors": ["красный","синий"]
# }
# print(products.keys())
# # for i in products.keys():
# #     print(f"{i} - {products[i]}")
# #     print(products.copy())
# products["name"] = "коврик"
# products["category"] = "ксессуары"
disciplines = ["eng","math","rus","lit"]
def show_dict(product):
    for i in product.keys():
        print(f"{i}")

def students_marks():
    st1 = {}
    for i in disciplines:
        st1[i] = []
        for j in range(random.randint(3,9)):
            st1[i].append(random.randint(2,5))
    return st1
def avg(list):
    sum = 0
    for i in list:
        sum += i
    return sum/len(list)
def best_disciplin_name(st):
    max = 0
    disc_name = "bbbbbnnmmm"
    for i in st.keys():
        avg.mark = avg(st[i])
        if max<avg.mark:
            max = avg.mark
            disc_name = i
    return  disc_name
def best_disciplin_name(st):
    max = 0
    disc_name = "bbbbbnnmmm"
    for i in (st.keys()):
        avg.mark = len(st[i])
        if max<avg.mark:
            max = avg.mark
            disc_name = i
    return disc_name

def disciplin_with_mark(st):
    ls = []
    for i in st.keys():
        avg.mark = avg(st[i])
        if avg.mark >= 3:
            ls.append(i)
    return  ls


st2 = students_marks()
show_dict(st2)
print(f"{disciplin_with_mark(st2)} оценка больше 3")
