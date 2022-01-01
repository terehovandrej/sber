def replace_whitespaces(sentence, symbol):
    arr = sentence.split(' ')
    is_replaced = True
    while is_replaced:
        is_replaced = False
        i = 0
        while i < len(arr) and len(arr) > 1:
            if symbol in arr[i] and i - 1 >= 0 and len(arr[i]) + 1 > len(arr[i - 1]):
                arr[i] = symbol * (len(arr[i]) + len(arr[i - 1]) + 1)
                arr.pop(i - 1)
                is_replaced = True
                continue
            elif symbol in arr[i] and i + 1 < len(arr) and len(arr[i]) + 1 > len(arr[i + 1]):
                arr[i] = symbol * (len(arr[i]) + len(arr[i + 1]) + 1)
                arr.pop(i + 1)
                is_replaced = True
                continue
            else:
                i += 1

    max_len = 0
    for v in arr:
        if symbol in v and len(v) > max_len:
            max_len = len(v)

    return max_len


print(replace_whitespaces('aaa bbb cc', 'a'))
