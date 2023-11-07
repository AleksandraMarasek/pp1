def max_dice_rolled_in_a_row(dice):
    if not dice:
        return 0

    max_count = 1 
    current_count = 1

    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 1

    return max(max_count, current_count)