# range(starting number, ending number, increment)

for i in range (0, 1000000, 25):
  print(i)

# Day20_Challenge:

print("""List Generator""")

start = int(input("Starting number > "))
end = int(input("Ending number > "))
increment = int(input("Increment between values > "))

for i in range(start, end, increment):
  print(i)
