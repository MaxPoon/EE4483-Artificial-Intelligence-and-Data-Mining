from math import factorial as f

def nCr(n,r):
	return f(n)/f(r)/f(n-r)

total = 0
for i in range(1,22):
	combinations_x = nCr(22,i)
	total_y=0
	for j in range(1,22-i):
		total_y+=nCr(22-i, j)
	total+=total_y*combinations_x
print(total)