# While this recursive solution works, it has a big O runtime of O(2^n).
# In the worst case, each step would require us to evaluate two subproblems,
# sometimes repeatedly, as there’s overlap between subproblems.
# We can drastically improve on this runtime by using dynamic programming.
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

# dynamic approach: using memoization
# will allow us to store information instead of making duplicate calls


def dynamic_knapsack(weight_cap, weights, values):
    rows = len(weights) + 1
    cols = weight_cap + 1
    # Set up 2D array
    matrix = [[] for x in range(rows)]

    # Iterate through every row
    for index in range(rows):
        # Initialize columns for this row
        matrix[index] = [-1 for y in range(cols)]

        # Iterate through every column
        for weight in range(cols):
            # Write your code here
            if index == 0 or weight == 0:
                matrix[index][weight] = 0
            elif matrix[index-1] <= weight:
                matrix[index][weight] = max

    # Return the value of the bottom right of matrix
    return matrix[rows-1][weight_cap]
