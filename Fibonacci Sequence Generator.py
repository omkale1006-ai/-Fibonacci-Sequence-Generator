'''
Program to print the Fibonacci sequence
'''

print("✨ Welcome to the Fibonacci Generator! ✨")
num = int(input("How many terms do you want? ➡ "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if num <= 0:
    print("⚠ Please enter a positive integer.")
elif num == 1:
    print(f"📜 Fibonacci sequence up to {num} term: {n1}")
else:
    print("📜 Fibonacci sequence:")
    while count < num:
        print(n1, end=" ")
        nth = n1 + n2
        # update values
        n1, n2 = n2, nth
        count += 1
    print("\n✅ Sequence generated successfully!")
