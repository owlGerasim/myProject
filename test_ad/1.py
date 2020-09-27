## первая задача
print("Введите длину")
n=float(input())
while(n<0):
    print("Введите длину")
    n=float(input())

print("Введите ширину")
m=float(input())
while(m<0):
    print("Введите ширину")
    m=float(input())

if(m>n):
    temp=n
    n=m
    m=temp
print("Введите растояние до от одного из длинных бортиков (не обязательно от ближайшего)")
x=float(input())
while(x<0)or(x>m):
    while(x<0):
        print("недопустимое значение")
        print("Введите растояние до от одного из длинных бортиков (не обязательно от ближайшего)")
        x=float(input())
    while(x>m):
        print("недопустимое значение")
        print("Введите растояние до от одного из длинных бортиков (не обязательно от ближайшего)")
        x=float(input())

print("Введите растояние до одного из коротких бортиков")
y=float(input())
while(y<0)or(y>n):
    while(y<0):
        print("недопустимое значение")
        print("Введите растояние до одного из коротких бортиков")
        y=float(input())
    while(y>n):
        print("недопустимое значение")
        print("Введите растояние до одного из коротких бортиков")
        y=float(input())

rez=[]
x1=m-x
x2=m-x1
y1=n-y
y2=n-y1
rez.append(x1)
rez.append(x2)
rez.append(y1)
rez.append(y2)

min=rez[0]
for i in range(1,len(rez)-1,1):
    if(rez[i]<min):
        min=rez[i]
print("Минимальное расстояние: ",min)