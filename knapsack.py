def recursive_knapsack(weight_cap, weights, values, i):
    # weight_cap or i are zero, meaning the knapsack can hold no weight,
    # or there are no more items to look at. In either case, we return 0.
    if weight_cap == 0 or i == 0:
        return 0
    # The weight of the item we’re looking at exceeds weight_cap,
    # in which case we just move on, calling the function on the next item.
    elif weights[i-1] > weight_cap:
        return recursive_knapsack(weight_cap, weights, values, i - 1)
    # we need to look at both situations and determine if we want to include this item
    # in our optimized solution or not.
    else:
        include_item = values[i-1] + recursive_knapsack(
            weight_cap - weights[i-1], weights, values, i - 1)
        exclude_item = recursive_knapsack(weight_cap, weights, values, i-1)

        return max(include_item, exclude_item)
