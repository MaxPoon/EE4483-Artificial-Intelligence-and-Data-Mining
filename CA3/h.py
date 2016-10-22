def support(d,m, n, prefix, suffix):
	if m==n:
		if prefix in d:
			d[prefix]+=1
		else:
			d[prefix]=1
	else:
		for i in range(len(suffix)-(n-m)+1):
			if m+1<n:
				support(d,m+1,n,prefix+suffix[i]+",", suffix[i+1:] )
			else:
				support(d,m+1,n,prefix+suffix[i], suffix[i+1:] )

def combinations_recursive(prefix,suffix,r, c):
	if r==len(prefix):
		c.append(prefix)
	else:
		for i in range(len(suffix)-(r-len(prefix))+1):
			combinations_recursive(prefix+[suffix[i]], suffix[i+1:],r,c)

def combinations(n,r):
	c = []
	combinations_recursive([],[i for i in range(n)],r,c)
	return c


def confidence(itemset, d, confidence_table, minsup=0):
	if d[itemset]<minsup:
		return
	itemList = itemset.split(',')
	if len(itemList)==1:
		return
	for r in range(1,len(itemList)):
		X_index = combinations(len(itemList),r)
		X_sets = []
		Y_sets = []
		for index in X_index:
			X_sets.append([])
			Y_sets.append([])
			for i in range(len(itemList)):
				if i in index:
					X_sets[-1].append(itemList[i])
				else:
					Y_sets[-1].append(itemList[i])
		for i in range(len(X_sets)):
			key = ','.join(X_sets[i])+'->'+','.join(Y_sets[i])
			value = d[itemset]/d[','.join(X_sets[i])]
			confidence_table[key] = value

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
confidence_table={}
for k,v in d.items():
	confidence(k, d, confidence_table,6)
for k,v in confidence_table.items():
	if v==1:
		print(k,v)