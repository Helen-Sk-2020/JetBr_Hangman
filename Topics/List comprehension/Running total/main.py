numbers = list(input())
list_numbers = [int(number) for number in numbers]
index = sum_ = 0
cumulative_sum = []
while True:
    sum_ += list_numbers[index]
    cumulative_sum.append(int(sum_))
    index += 1
    if index == len(list_numbers):
        break
print(cumulative_sum)
