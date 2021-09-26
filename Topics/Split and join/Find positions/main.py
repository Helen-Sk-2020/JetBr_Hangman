numbers = input().split()
number = str(input())
position = []
if number in numbers:
    position = [str(i) for i, x in enumerate(numbers) if x == number]
    print(' '.join(position))
else:
    print("not found")
    