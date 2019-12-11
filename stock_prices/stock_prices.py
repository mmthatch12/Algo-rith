#!/usr/bin/python

import argparse

def find_max_profit(prices):
  maxi = max(prices)
  mini = min(prices)
  test = 1
  if prices.index(maxi) > prices.index(mini):
    return maxi - mini
  else: 
    counter = -5000
    for i in range(len(prices)-1):
      for j in range(test, len(prices)):
        cprice = -prices[i] + prices[j]
        if cprice > counter:
          counter = cprice
      test+=1
    print("counter", counter)
    return counter
  

  # for i in range(len(prices)):


print(find_max_profit([10, 7, 5, 8, 11, 9]))



# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

# elif prices.index(maxi) < prices.index(mini):
#     nprices = prices[prices.index(maxi)+1:]
#     print('nprices', nprices)
#     nmaxi = max(nprices)
#     if nprices.index(nmaxi) > nprices.index(mini):
#       return nmaxi - mini
#     elif nprices.index(nmaxi) < nprices.index(mini):
#       mprices = nprices[:]
#       nmini = min(mprices)
#       if mprices.index(nmaxi) > mprices.index(nmini):
#         return nmaxi - mini 