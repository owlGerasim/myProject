#четвёртая задача
print("Введите IP")
a=input()
a=a.split(sep=".")
flag=True
for  i in range(len(a)):
	if(str(a[i]).isdigit()):
		if(int(a[i])>0)and(int(a[i])<256):
			flag=True
		else:
			flag=False
			break
	else:
		flag=False
		break
if flag:
	print("YES, is IP")
else:
	print("NO, Is not IP")
