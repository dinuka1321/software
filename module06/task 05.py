def remove_odds(numbers):
    return [num for num in numbers if num % 2 == 0]


def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    filtered = remove_odds(nums)
    print("Original list:", nums)
    print("Even numbers only:", filtered)

main()