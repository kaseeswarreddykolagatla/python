def maxprofit(prices):
    n = len(prices)
    if n < 2:
        return 0

    left = [0] * n
    right = [0] * n

    minprice = prices[0]
    for i in range(1,n):
        left[i] = max(left[i - 1], prices[i] - minprice)
        minprice =min(minprice, prices[i])

    maxprice =prices[n -1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], maxprice - prices[i])
        maxprice = max(maxprice, prices[i])

    maxprofit = 0
    for i in range(n):
        maxprofit = max(maxprofit, left[i] + right[i])

    return maxprofit

prices = [7,1,5,3,6,4]
print("Maximum profit: ", maxprofit(prices))
