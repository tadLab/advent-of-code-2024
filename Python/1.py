with open("2024/1.txt", "r") as file:
    right_numbers = []
    left_numbers = []

    for line in file:
        line = line.strip()
        numbers = line.split("   ")
        print(numbers)
        right_numbers.append(int(numbers[0]))
        left_numbers.append(int(numbers[1]))

#print(right_numbers)
#print(left_numbers)

sorted_right_numbers = sorted(right_numbers)
sorted_left_numbers = sorted(left_numbers)

#print(sorted_right_numbers)
#print(sorted_left_numbers)

total_distance = 0

for i in range(len(sorted_right_numbers)):
    total_distance += abs(sorted_right_numbers[i] - sorted_left_numbers[i])

print(total_distance)
        
