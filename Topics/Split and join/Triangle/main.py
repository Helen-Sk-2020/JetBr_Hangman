height = int(input())
counter = 0
row = '#'
width = 1 + (height - 1) * 2
while height > counter:
    counter += 1
    print(row.center(width, ' '))
    row += '#' * 2
    