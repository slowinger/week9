import random


def sort(items):
    stop = False
    while stop is False:
        for i in range(len(items) - 1):
            if i == 0:
                swaps = 0
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i+1], items[i]
                swaps += 1
        if swaps == 0:
            stop = True
    return items




numbers = list(range(10))
random.shuffle(numbers)

assert list(range(10)) == sort(numbers)
print("The list was sorted correctly!")

# 2. Change this print statement to display the complexity category.
#    Refer to the cheat sheet in week9-class for examples.
print("This algorithm is classified as: O(n^2)")
