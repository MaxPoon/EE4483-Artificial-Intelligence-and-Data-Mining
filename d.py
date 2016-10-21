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
twelve, ten, five=0,0,0
for k,v in d.items():
	if v>= 0.12*150:
		twelve+=1
	if v>=0.1*150:
		ten+=1
	if v>=0.05*150:
		five+=1
print(twelve,ten, five)