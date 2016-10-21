def support(d,m, n, prefix, suffix):
	if m==n:
		if prefix in d:
			d[prefix]+=1
		else:
			d[prefix]=1
	else:
		for i in range(len(suffix)-(n-m)+1):
			if m+1<n:
				support(d,m+1,n,prefix+suffix[i]+", ", suffix[i+1:] )
			else:
				support(d,m+1,n,prefix+suffix[i], suffix[i+1:] )

transactions = []
i = 0
with open('grocery.basket.txt','r') as f:
	for line in f:
		transactions.append([])
		for word in line.split(','):
			w = word
			if w[-1]=='\n':
				w=w[:-1]
			transactions[i].append(w)
		i+=1
for transaction in transactions:
	transaction.sort()
d = {}
for transaction in transactions:
	for i in range(1,len(transaction)):
		support(d,0,i,"",transaction)
total = 0
four = 0
three = 0
two = 0
for k,v in d.items():
	if v>=0.02*150:
		total+=1
		if k.count(',')==3:
			four+=1
		if k.count(',')==2:
			three+=1
		if k.count(',')==1:
			two+=1
print(four/total,three/total,two/total)