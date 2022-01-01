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
            elif znak == '//' and num != 0:
                tmp //= num
            # elif znak == '//' and num == 0:
            #     tmp = 0
            #     break

        if tmp > result:
            result = tmp

    return result


print(calculation([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],
                  ['+', '+', '+', '*', '*', '*', '+', '+', '+', '*', '*', '*', '+', '+', '+', '*', '*', '*', '+', '+',
                   '+', '*', '*', '*', '//']))
