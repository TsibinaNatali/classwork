def list1(ls1,ls2):
    set1 = set()
    for i in ls1:
        if i in ls2:
            set1.add(i)
    return set1

def count_str(str1):
    rez = str1.




clova = {'hello', 'daddy', 'hello', 'mum''hello', 'daddy', 'hello', 'mum'}
clova2 = {'hello', 'daddy', 'mum', "dfdg", "kjlio","gfhfhf"}

print(list1(clova,clova2))
print(set(clova).intersection(set(clova2)))

stroka = 'hello', 'daddy', 'hello', 'mum''hello', 'daddy', 'hello', 'mum'