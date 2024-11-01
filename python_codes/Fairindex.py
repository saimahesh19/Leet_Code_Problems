def fairindex(a, b):
    if len(a) != len(b):
        return 0

    n = len(a)
    total_a = sum(a)
    total_b = sum(b)

    if total_a != total_b:
        return 0

    left_sum_a = 0
    left_sum_b = 0
    fair_count = 0

    for k in range(1, n):
        left_sum_a += a[k - 1]
        left_sum_b += b[k - 1]
        
        right_sum_a = total_a - left_sum_a
        right_sum_b = total_b - left_sum_b

        if left_sum_a == right_sum_a and left_sum_b == right_sum_b and left_sum_a == left_sum_b:
            fair_count += 1

    return fair_count
