the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quaters']

# this first kind of for-loop goes through the list
for number in the_count:
	print(f'This is the count {number}')

# same as above.
for fruit in fruits:
	print(f"A fruit of type: {fruit}")

# also we can go through mised lists too
for i in change:
	print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print(f"Adding {i} to the lists")
	# append is a function that list understands
	if i == 0:
		elements.insert(0, 100)
	elements.append(i)

# print(elements)

for i in elements:
	print(f"Element was: {i}")

