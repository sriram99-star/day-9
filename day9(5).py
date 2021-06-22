n = int(input('Enter number: ')) 
for i in range(n): 
	print(''.join(map(str,range(n-i,0,-1)))) 
