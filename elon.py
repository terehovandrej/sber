from collections import Counter


def get_result(rocket_pos, rocket_speed):
    result = 0

    while min(rocket_pos) <= 1000:
        counter = Counter(rocket_pos)
        for k, v in counter.items():
            if v > 1:
                indexes = []
                for i, pos in enumerate(rocket_pos):
                    if k == pos:
                        indexes.append(i)

                speed_sum = 0
                for i in indexes:
                    speed_sum += rocket_speed[i]

                rocket_pos = list(filter(lambda x: x != int(k), rocket_pos))
                rocket_pos.append(int(k))

                rocket_speed = [rocket_speed[i] for i in range(len(rocket_speed)) if i not in indexes]
                rocket_speed.append(speed_sum)
                result += v

        for i in range(len(rocket_pos)):
            rocket_pos[i] += rocket_speed[i]

    return result


print(get_result([1, 5, 5, 2, 4, 4, 4], [10, 10, 10, 10, 20, 30, 40]))
