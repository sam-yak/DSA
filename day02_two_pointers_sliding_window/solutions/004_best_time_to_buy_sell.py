def max_profit(prices):
    min_price=prices[0]
    max_profit= 0
    for price in prices:
        min_price=min(min_price, price)
        profit = price - min_price
        max_profit=max(max_profit, profit)
    return max_profit
if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([2, 4, 1]) == 2
    print("All tests passed!")
