from itertools import permutations


def calculation(arr, znaks):
    znak_comb = set(permutations(znaks))
    result = 0
    for zn in znak_comb:
        tmp = 0
        for znak, num in zip(zn, arr):
            if znak == '+':
                tmp += num
            elif znak == '-':
                tmp -= num
            elif znak == '*':
                tmp *= num
            elif znak == '//':
                tmp //= num

        if tmp > result:
            result = tmp

    return result


print(calculation([10, 4, 1], ['+', '-', '*']))
