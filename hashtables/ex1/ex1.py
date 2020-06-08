def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    storage = {}

    for index in range(length):
        other_weight = limit - weights[index]

        if other_weight in storage:
            other_index = storage[other_weight]
            return (index, other_index)
        else:
            storage[weights[index]] = index

    return None

# Forgot to checkout to working ... agian ...
