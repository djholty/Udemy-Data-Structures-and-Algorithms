#find the lowest number of coins given a set of denominations and a total dollar value
#an example of a greedy algorithm

def coinChange(totalNumber, coins):
    N = totalNumber
    coinNum = 0
    coins.sort()
    index = len(coins) -1
    while True:
        coinValue = coins[index]
        if N >= coinValue:
            N = N - coinValue
            coinNum += 1
        if N < coinValue:
            index -= 1
        if N == 0:
            break
    print(f"The total number of coins needed is {coinNum}")

coins = [1,2,5,20,50,100]
coinChange(201, coins)

