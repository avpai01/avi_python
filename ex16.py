from sys import argv
script, filename = argv

print(f"'We're going to erase the {filename}")
print("If you do not want that, hit CTRL-C (^C)")
print("If you do want that, hit RETURN")

input('?')

print("Opening the file...")
target = open(filename, 'a')

print("Truncating the file. Goodbye!")
# target.truncate()

print("Now I am going to add few line")

line1 = input("Line 1:")
line2 = input("Line 2:")
line3 = input("Line 3:")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print("And finally we close it.")
target.close()
