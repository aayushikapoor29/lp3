def fractional_knapsack(values, weights, capacity):
    n = len(values)
    ratio = []

    for i in range(n):
        ratio.append((values[i]/weights[i], values[i], weights[i]))

    ratio.sort(reverse=True)

    total_value = 0.0

    for r, v, w in ratio:
        if capacity >=w:
            capacity -= w
            total_value += v
        else:
            total_value += r * capacity
            break
    return total_value


value = [60, 100, 120]
weight = [10, 20, 30]
cap = 50

max_value = fractional_knapsack(value, weight, cap)
print(f"Maximum value in Knapsack = {max_value}")

