# Solving an exercise involving buying and selling stocks listed in an array
# Goal is to calculate the combinating of two days (one buy and one sell) in which the most profit would be yielded

def buy_and_sell_one(listOfPrices):
    maxProfit = 0
    minPrice = float('inf')

    for price in listOfPrices:
        minPrice = min(minPrice, price)
        temp_Profit = price - minPrice
        maxProfit = max(maxProfit, temp_Profit)
    return maxProfit

