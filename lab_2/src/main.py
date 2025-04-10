def max_hamsters(daily_food, total_hamsters, hamster_data):
    def can_feed(selected_count):
        food_needed = []
        for i in range(selected_count):
            base_food, greed = hamster_data[i]
            food_needed.append(base_food + greed * (selected_count - 1))
        food_needed.sort()
        return sum(food_needed) <= daily_food

    hamster_data.sort(key=lambda x: x[0] + x[1] * (total_hamsters - 1))
    min_hamsters, max_hamsters = 0, total_hamsters
    while min_hamsters < max_hamsters:
        mid_hamsters = (min_hamsters + max_hamsters + 1) // 2
        if can_feed(mid_hamsters):
            min_hamsters = mid_hamsters
        else:
            max_hamsters = mid_hamsters - 1
    return min_hamsters
