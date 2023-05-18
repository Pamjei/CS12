memo = {}
cost = [0, 3, 4, 6, 10]
value = [0, 1, 2, 3, 4]
n = 4
C = 4

def knapsack(i, c):
    if i == 0 and c < cost[i]:
        return 0
    if i == 0 and c >= cost[i]:
        return value[i]
    if (i, c) in memo:
        return memo[(i, c)]

    max_choice = knapsack(i - 1, c)  # skip ith item
    if c >= cost[i]:  # check if ith item is affordable
        max_choice = max(max_choice, knapsack(i - 1, c - cost[i]) + value[i])
    memo[(i, c)] = max_choice
    return max_choice


def knapsack_reconstruct(i, c):  # assumes knapsack has been run
    ind = i
    capacity = c
    items = []
    while ind > 0:
        if capacity >= cost[ind] and memo[(ind - 1, capacity - cost[ind])] + value[ind] > memo[(ind - 1, capacity)]:
                items.append(ind)
                capacity -= cost[ind]
        ind -= 1
    if capacity > cost[ind]:
        items.append(ind)
    return reversed(items)
                
                
print(knapsack(n - 1, 4))
items = knapsack_reconstruct(n - 1, 4)
print('Items chosen are (indices):', ','.join([str(n) for n in items]))
