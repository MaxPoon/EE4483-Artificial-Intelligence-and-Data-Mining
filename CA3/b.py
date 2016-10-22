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
maxSize = 1
for i in range(150):
	if len(transactions[i]) > maxSize:
		maxSize = len(transactions[i])
print(maxSize)
for transaction in transactions:
	if len(transaction)==maxSize:
		print(transaction)