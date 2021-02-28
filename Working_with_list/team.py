def team():
		n = int(input())
		while n > 0:
			teamstat = input()
			sum = 0
			surity = [x for x in teamstat if x != ' ']
			count = surity.count('1')
			n -= 1
		for i in range(n):
			if count >= 2:
				sum += 1
		print(sum)
	team()
