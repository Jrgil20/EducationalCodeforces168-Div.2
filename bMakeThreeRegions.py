# make three regions



cases = int(input())
while cases < 1 or cases > 10000:
    cases = int(input("Invalid input. Please enter a number between 1 and 10000: "))

for _ in range(cases):
    n = input()
    while n < 1 or n > 100000:
        n = int(input("Invalid input. Please enter a number between 1 and 100000: "))
    
    