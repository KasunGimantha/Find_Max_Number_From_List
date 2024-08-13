numbers = input(
    "Copy and paste your list of numbers(with spaces): ").split(" ")


def max_num(numbers):

    max_value = numbers[0]

    for num in numbers[1:]:
        if (num > max_value):
            max_value = num
    return max_value


print(f"Max number is {max_num(numbers)}")
