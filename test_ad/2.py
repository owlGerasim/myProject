#вторая задача
lenkrug=109
print("Введите скорость")
v=int(input())
while(v<-1000)or(v>1000):
    print("Неверно")
    print("Введите скорость")
    v=int(input())
print("Введите время")
t=int(input())
while(t<0)or(t>1000):
    print("Неверно")
    print("Введите время")
    t=int(input())
s=v*t
if(v>=0):
    print("Отметка: ",s-lenkrug*(s//lenkrug))
else:
    print("Отметка: ",lenkrug-(lenkrug-(s-lenkrug*(s//lenkrug))))