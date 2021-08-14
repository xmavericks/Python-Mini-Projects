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

------- Output --------
Test: #1, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
8
Output
YES
Answer
YES
Checker Log
ok answer is YES
Test: #2, time: 92 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
Input
5
Output
NO
Answer
NO
Checker Log
ok answer is NO
