numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
not_number = numbers.index(None)
count = len(numbers)
total_sum = sum(numbers[:not_number]) + sum(numbers[not_number + 1:])
average = total_sum / count
numbers[not_number] = average
print("Измененный список:", numbers)
