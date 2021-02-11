n = int(input("Enter any natural number you want: "))

def check_even_odd(n):
  if n % 2 == 0:
    return "Even"
  else:
    return "Odd"

print(check_even_odd(n))
