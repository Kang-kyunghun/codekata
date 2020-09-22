def maxProfit(prices):
    result = []
    for i_buy in range(len(prices)):
        for i_sale in range(i_buy +1, len(prices)):
            result.append(prices[i_sale] - prices[i_buy])
            print(prices[i_sale], prices[i_buy])
    print(result)
    return max(result) if max(result) > 0  else 0

prices = [7,6,4,3,1] 
print(maxProfit(prices))

'''
모범답안
def maxProfit(prices): 
  max_profit, min_price = 0, float('inf')
  
  for price in prices:
      min_price = min(min_price, price)
      profit = price - min_price
      max_profit = max(max_profit, profit)
      
  return max_profit
  '''