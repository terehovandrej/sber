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
        fl = False
        i = 0
        tmp_matches = s
        while i < len(s):
            tmp = s[0:i:] + s[i + 1::]
            matches = calculate_matches(tmp, string_goal)
            if matches > max_matches:
                tmp_matches = tmp
                max_matches = matches
                fl = True
            i += 1
        counter += 1
        if not fl:
            s = s[1::]
        else:
            s = tmp_matches
    return max_matches


print(get_result('aaaaabb', 5, 'bb'))
