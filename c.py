def support(d,m, n, prefix, suffix):
	'''
	d: dictionary: hash table to store the support of each combination
	m: number of item that has already been chosen
	n: int: the size of the itemset
	prefix: str: a string of all the chosen item. 
			If we have chosen Apple and Olive, prefix will be 'AppleOlive'
	suffix: list: the item that can be chosen
	return: list: [most frequent itemset, support of most frequent itemset]
	'''
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
	if  len(transaction)<2:
		continue
	support(d,0,2,"",transaction)
max_2_support = max(d.values())
print("The maximum support of 2-itemset is: "+ str(max_2_support))
print("The 2-itemset(s) having support of "+str(max_2_support)+" are:")
for k,v in d.items():
	if v==max_2_support:
		print(k) 

print()
d = {}
for transaction in transactions:
	if  len(transaction)<3:
		continue
	support(d,0,3,"",transaction)
max_3_support = max(d.values())
print("The maximum support of 3-itemset is: "+ str(max_3_support))
print("The 3-itemset(s) having support of "+str(max_3_support)+" are:")
for k,v in d.items():
	if v==max_3_support:
		print(k) 