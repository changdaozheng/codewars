
def capitalize(s): 
	#registering letters
	text = []
	for char in s:
		text.append(char)

	#even caps 
	even = []
	for i in len(text): 
		if i % 2 == 0:
			even.append(upper(text[i]))
		else:
			even.append(text[i])

	#odd
	odd = []
	for i in len(text): 
		if i % 2 == 1:
			odd.append(upper(text[i]))
		else:
			odd.append(text[i])


	return [''.join(even), ''.join(odd)]
