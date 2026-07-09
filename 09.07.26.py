
# def begin(st):
#      return st[st.find("begin")+5: st.find("end")]
#
#
# def begin1(st):
#
#     return st[st.find("begin") + 5: st.find("end")]





# st = "jhgjkhhj begin gjhuhjh hjklkj end jhjh"
# print(begin(st))
#
# st = ["Вдохновение","Благодать","Млечнич","Заревна","Перламуфла","Искренновна","Гармония", "Шепотовна","Ностальгия","Лазуровна"]
# # for i in st:
# #     if i[1:1] == "овна":
# #         print(i)
# qlas = "аеоиёуэюя"
# for i in st:
#     for i[0] in glas:
#         print(i)
# st = "Если сделал уроки и помыл посуду можешь идти гулять!"
# st2=" "
# list = st.split(" ")
# for i in list:
#     if i != " " and i[-1:] == "л":
#         i += "a"
#     st2 += i+" "
#     st2 = st2.strip()
# print(st2)
st = "апельсин мандарин тоже фрукт 4 что и мандарин"
s = set(st.split(" "))
str=""
for i in s:
    if i != "":
        str+=i+" "

print(str.strip().split(" "))

for i in st :
    count=0
    if i.isdigit():
        count+=1
print(count)