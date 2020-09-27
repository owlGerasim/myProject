# третье задание
print("введите количество эллементов массива")
n=int(input())
print("Введите элементы массива")
a=[]
for i in range (0,n,1):
    i=input()
    a.append(i)
for i in range (0,n,1):
    if(a.count(a[i])==1):
        print(a[i],end=' ')