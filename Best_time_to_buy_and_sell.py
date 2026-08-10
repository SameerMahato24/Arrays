def best(arr):
    max_profit = 0
    min_price = float('inf')
    for price in arr:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit
    

print(best([7,2,1,0,5,6,4,8]))