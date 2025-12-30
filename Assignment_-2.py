''' Task-1: Check if a Number is Even or Odd'''

print("odd and even number checking:-")
# Giving input
num = int(input("Enter a number: "))

# Putting result
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
print()

'''Task-2'''
print("Looping and sum:-")
total = 0

for i in range(1, 51):
    total += i  # Add each number to the total

print(f"The sum of numbers from 1 to 50 is: {total}")

