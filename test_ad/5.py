#пятая задача
print("Введите количество элементов первого массива")
n1=int(input())
a1=[]
for i in range(n1):
	print("Введите элементы первого массива")
	a1=a1+[int(input())]

print("Введите количество элементов второго массива")
n2=int(input())
a2=[]
for i in range(n2):
	print("Введите элементы второго массива")
	a2=a2+[int(input())]
c = list(set(a1) & set(a2))
print(c)