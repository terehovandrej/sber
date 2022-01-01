def calculate_matches(tmp_str, goal_str):
    counter = 0
    for ts, gs, in zip(tmp_str, goal_str):
        if ts == gs:
            counter += 1

    return counter


def get_result(s: str, k: int, string_goal: str):
    counter = 0
    max_matches = 0
    while counter < k:
        i = 0
        tmp_matches = s
        while i < len(s):
            tmp = s[0:i:] + s[i + 1::]
            matches = calculate_matches(tmp, string_goal)
            if matches > max_matches:
                tmp_matches = tmp
                max_matches = matches
            i += 1
        counter += 1
        s = tmp_matches
    return max_matches


print(get_result('agdadb', 5, 'gddr'))
