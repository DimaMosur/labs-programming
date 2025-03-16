def max_hamsters(S, C, hamsters):
    def can_feed(count):
        food_needed = []
        for i in range(count):
            H, G = hamsters[i]
            food_needed.append(H + G * (count - 1))
        food_needed.sort()
        return sum(food_needed) <= S

    hamsters.sort(key=lambda x: x[0] + x[1] * (C - 1))
    left, right = 0, C
    while left < right:
        mid = (left + right + 1) // 2
        if can_feed(mid):
            left = mid
        else:
            right = mid - 1
    return left