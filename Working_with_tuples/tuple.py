# Definition File
Tuples~

Tuples are very similar to lists, except that they are immutable (they cannot be changed).
Also, they are created using parentheses, rather than square brackets.

Example:
words = ("spam", "eggs", "sausages")

You can access the values in the tuple with their index, just as you did with lists:
 
print(words[0]) // gives output as :: spam


Re-assigning value:

Trying to reassign a value in a tuple causes an error.
words[0] = "maggi"

Error message - 
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    words[0] = "maggi"
TypeError: 'tuple' object does not support item assignment


Note - Like lists and dictionaries, tuples can be nested within each other
Example:
words = ("spam",("maggi","masala"))
print(words[1])

--- Output---
('maggi', 'masala')

Advantage of tuple over List:
~ An advantage of tuples over lists is that they can be used as keys for dictionaries (because they are immutable)
~ Tuples are faster than lists, but they cannot be changed.

Example :
dict = {
    ("David", 42): "red",
    ("Bob", 24): "green"
}

print(dict[("Bob", 24)])

---- Output ----
green
