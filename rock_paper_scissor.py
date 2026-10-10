
def count_positives_sum_negatives(arr):
    if not arr:
        return []

    positives = 0
    negatives_sum = 0

    for value in arr:
        if value > 0:
            positives += 1
        elif value < 0:
            negatives_sum += value

    return [positives, negatives_sum]