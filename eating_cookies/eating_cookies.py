#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
cachee = {}
def eating_cookies(n, cache=None):
  
  if n <= 1:
    return 1
  if n == 2:
    return 2

  if n not in cachee:
    cachee[n] = eating_cookies(n-1)+eating_cookies(n-2)+eating_cookies(n-3)
  
  return cachee[n]



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')

# if n = 0 => 1
# if n = 1 => 1
# if n = 2 => 2
# if n = 3 => 4
# if n = 4 => 7
# combo of ones can only happen in one way
# if n is even combo of 2 can only happen 1 way, else no ways
# if n is divisible by 3 combo of 3 can only happen 1 way, else no ways

# n=1
# 1

# n=2
# 11
# 2

# n = 3
# 111
# 21
# 12
# 3

# n=4
# 1111
# 211
# 121
# 31
# 112
# 22
# 13


# n = 4 => 7
# only ones = 1[1,1,1,1]
# only twos = 1[2,2]
# ones and twos = 3[1,1,2][1,2,1][2,1,1]
# ones and threes = 2[3,1][1,3]

# n= 5 => 13

# only ones= only ever on way 1 [1,1,1,1,1]
# only twos and ones =      7 [2,1,1,1][1,2,1,1][1,1,2,1][1,1,1,2][2,2,1][2,1,2][1,2,2]
# only ones and threes = 3 [1,3,1][1,1,3][3,1,1]
# only twos and threes = 2 [3,2][2,3]

# n = 6 => 22

# only ones = 1 [1,1,1,1,1,1]
# only twos = 1 [2,2,2]
# only threes = 1[3,3]
# only ones and twos = 10[1,1,1,1,2][1,1,1,2,1][1,1,2,1,1][1,2,1,1,1][2,1,1,1,1][2,2,1,1][2,1,1,2][1,1,2,2][1,2,1,2][2,1,2,1]
# only ones and threes = 4[3,1,1,1][1,1,1,3][1,1,3,1][1,3,1,1]
# only twos and threes = 0
# all = 5[3,2,1][1,2,3][2,1,3][3,1,2][1,3,2]


