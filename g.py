def combinations_recursive(prefix,suffix,r, c):
	if r==len(prefix):
		c.append(prefix)
	else:
		for i in range(len(suffix)-(r-len(prefix))+1):
			combinations_recursive(prefix+[suffix[i]], suffix[i+1:],r,c)

c = []
combinations_recursive([],[0,1,2,3,4,5],3,c)
print(c,len(c))