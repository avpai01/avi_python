def add(a, b):
	print(f"Adding {a} and {b}")
	return a + b

def subtract(a, b):
	print(f"Subtracting {a} - {b}")
	return a - b

def multiply(a, b):
	print(f"Multiplying {a} * {b}")
	return a * b

def divide(a, b):
	print(f"Dividing {a} / {b}")
	return a / b

print("Let's do some math with just functions!")

age = add(20, 10)
height = subtract(100, 10)
weight = multiply(100, 10)
iq = divide(100, 10)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq} ")

# A puzzle for the extra credit, type it in anyway.
print("Here is the puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 10))))
print("That becomes:", what, "Can you do it by hand?")