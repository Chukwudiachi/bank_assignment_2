numbers = [70, 68, 99,  89, 34]

highest = numbers[0]


for number in numbers:

    if number > highest:
        highest = number


print(f"The largest number in the list is {highest}")
