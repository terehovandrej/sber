def get_result(schema):
    for i, s in enumerate(schema):
        schema[i] = [1] + [int(i) for i in s.split('-')] + [1]
    schema.insert(0, [1 for i in range(len(schema[0]))])
    schema.insert(len(schema), [1 for i in range(len(schema[0]))])

    cost = 0
    for i in range(1, len(schema) - 1):
        for j in range(1, len(schema[0]) - 1):
            if schema[i][j] and not schema[i][j - 1] and not schema[i - 1][j] and schema[i][j + 1] and schema[i + 1][j]:
                cost += 17
                print(cost)
            if schema[i][j] and schema[i][j - 1] and not schema[i - 1][j] and schema[i][j + 1] and schema[i + 1][j]:
                cost += 32
                print(cost)
            if schema[i][j] and schema[i][j - 1] and not schema[i - 1][j] and not schema[i][j + 1] and schema[i + 1][j]:
                cost += 10
                print(cost)
            if schema[i][j] and not schema[i][j - 1] and schema[i - 1][j] and schema[i][j + 1] and schema[i + 1][j]:
                cost += 40
                print(cost)
            if schema[i][j] and schema[i][j - 1] and schema[i - 1][j] and schema[i][j + 1] and schema[i + 1][j]:
                cost += 63
                print(cost)
            if schema[i][j] and schema[i][j - 1] and schema[i - 1][j] and not schema[i][j + 1] and schema[i + 1][j]:
                cost += 31
                print(cost)
            if schema[i][j] and not schema[i][j - 1] and schema[i - 1][j] and schema[i][j + 1] and not schema[i + 1][j]:
                cost += 15
                print(cost)
            if schema[i][j] and schema[i][j - 1] and schema[i - 1][j] and schema[i][j + 1] and not schema[i + 1][j]:
                cost += 29
                print(cost)
            if schema[i][j] and schema[i][j - 1] and schema[i - 1][j] and not schema[i][j + 1] and not schema[i + 1][j]:
                cost += 13
                print(cost)
            if schema[i][j] and not schema[i][j - 1] and schema[i - 1][j] and not schema[i][j + 1] and schema[i + 1][j]:
                cost += 20
                print(cost)
            if schema[i][j] and schema[i][j - 1] and not schema[i - 1][j] and schema[i][j + 1] and not schema[i + 1][j]:
                cost += 21
                print(cost)
    return cost


print(get_result(['0-0-0-0', '1-1-1-0', '0-0-1-0', '0-0-1-0']))
