with open("2024/1.txt", "r") as file:
    right_numbers = []
    left_numbers = []

    # Loop through the file and append the right and left numbers to their respective lists
    for line in file:
        line = line.strip()
        numbers = line.split("   ")
        # Debugging
        #print(numbers)
        right_numbers.append(int(numbers[0]))
        left_numbers.append(int(numbers[1]))

# Debugging
#print(right_numbers)
#print(left_numbers)

sorted_right_numbers = sorted(right_numbers)
sorted_left_numbers = sorted(left_numbers)

# Debugging
#print(sorted_right_numbers)
#print(sorted_left_numbers)

total_distance = 0

# Loop through the sorted right numbers and calculate the total distance
for i in range(len(sorted_right_numbers)):
    total_distance += abs(sorted_right_numbers[i] - sorted_left_numbers[i])

print(total_distance)
        
