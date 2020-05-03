def iq_test(numbers):
    numbers = list(map(int,numbers.split(' ')))
    numbers = [True if i % 2 == 0 else False for i in numbers]
    return numbers.index(False) + 1 if sum(numbers) > 1 else numbers.index(True) + 1

