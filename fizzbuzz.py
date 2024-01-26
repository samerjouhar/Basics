for i in range(1, 100):
	s = ""
	if i%3:
		s += "Fizz"
	if i%5:
		s += "Buzz"
	if s:
		print(s)
	else:
		print(i)
