def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = 0
    count = 0
    for number in numbers:
        try:
            total += float(number)  # Convert to float and handle potential errors
            count += 1
        except (ValueError, TypeError):
            print(f"Skipping non-numeric value: {number}")
            continue  #Skip non-numeric values
    if count == 0:
      return 0
    average = total / count
    return average

# Example usage:
my_list = [10, 20, 30, 0]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average = calculate_average(my_empty_list)
print(f"The average is: {average}")

my_list_with_string = [10, 20, 'a', 30, 40]
average = calculate_average(my_list_with_string)
print(f"The average is: {average}")