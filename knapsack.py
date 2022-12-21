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

# matrix = 2D array with rows equal to number of items and empty columns
# for every number of items you can carry (index):
#   fill matrix[index] with an array of length weight_cap + 1
#   for every weight < weight_cap (weight):
#     if index or weight == 0:
#       set element at [index][weight] to 0
#     else if the weight of element at index - 1 <= weight:
#       find possible values of including and excluding the item
#       set element at [index][weight] to max of those values
#     else:
#       set element at [index][weight] to element one above
# return element at bottom right of matrix


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
            elif weights[index-1] <= weight:
                matrix[index][weight] = max(values[index-1] + matrix[index-1][weight - weights[index-1]],
                                            matrix[index-1][weight])
            else:
                matrix[index][weight] = matrix[index-1][weight]

    # Return the value of the bottom right of matrix
    return matrix[rows-1][weight_cap]


if __name__ == "__main__":
    # Use this to test your function:
    weight_cap = 50
    weights = [31, 10, 20, 19, 4, 3, 6]
    values = [70, 20, 39, 37, 7, 5, 10]
    print(dynamic_knapsack(weight_cap, weights, values))
