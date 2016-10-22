from math import factorial as f

def nCr(n,r):
	return f(n)/f(r)/f(n-r)

total = 0
for i in range(1,11):
	total+= nCr(22,i)*2
total+=nCr(22,11)+1
print(total)