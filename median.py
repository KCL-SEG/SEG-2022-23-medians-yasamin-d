"""Median calculator."""


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
numbers.sort()

if len(numbers)%2 == 0:
    position = int(len(numbers)/2) -1
    median = (numbers[position] + numbers[position+1])/2
    print(median)


else:
    position = ((len(numbers) +1)/2) -1
    print(numbers[int(position)])
