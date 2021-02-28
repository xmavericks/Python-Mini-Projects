def main():
	n = int(input())
	def team(n):
		sum = 0
		while n > 0:
			teamstat = input()
			surity = [x for x in teamstat if x == '0' or x == '1']
			count = 0
			for value in surity:
				if value == '1':
					count = surity.count(value)
				else:
					count += 0
			if count >= 2:
				sum += 1
			
			n -= 1
			
		print(sum)
	team(n)
if __name__ == "__main__":
	main();
  
  
