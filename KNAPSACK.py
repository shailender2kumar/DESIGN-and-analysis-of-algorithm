def Knapsack(List_of_weights, List_of_profits, Capacity):
    n = min(len(List_of_weights), len(List_of_profits))
    s_a = [(List_of_weights[i], List_of_profits[i]) for i in range(n)]
    s_a.sort(key=lambda i: i[1], reverse=True)
    
    total_profit = 0
    result = []

    for item in s_a:
        if item[0] <= Capacity:
            total_profit += item[1]
            Capacity -= item[0]
            result.append(item)

    return (result, total_profit)

weights = [1, 12, 7, 5]
profits = [200, 100, 300, 150]
weight = 11
print(Knapsack(weights, profits, weight))
