import matplotlib.pyplot as plt

# Item 2a):
def maguffinPurchase1(total_money):
  return int(-0.5 + (0.25 + 2 * total_money) ** 0.5)

# Test cases
print('Item 2a):')
print(maguffinPurchase1(1))  # Output: 1
print(maguffinPurchase1(3))  # Output: 2
print(maguffinPurchase1(1000),'\n')  # Output: 44

# Item 2b):
def ln(x):
  n = 100000
  # Approximate the value of ln(x) using limit identity of the natural logarithm:
  return n * ((x ** (1/n)) - 1)

def log2(x):
  return ln(x) / ln(2)


def maguffinPurchase2(total_money):
  return int(log2(total_money + 1))

# Test cases:
print('Item 2b):')
print(maguffinPurchase2(1))  # Output: 1
print(maguffinPurchase2(3))  # Output: 2
print(maguffinPurchase2(1000),'\n')  # Output: 9

# Item 2c):
num_calls = 2 # Number of calls to maguffinPurchase3

# Defining maguffinPrice and maguffinTotalPrice as lambda functions for scenarios (1) and (2) above:
maguffinPrice_1 = lambda x: x # Linear pricing
maguffinPrice_2 = lambda x: 2 ** x # Exponential pricing
maguffinTotalPrice_1 = lambda x: x * (x + 1) / 2 # Sum of first x natural numbers
maguffinTotalPrice_2 = lambda x: 2 ** x - 1 # Sum of sequence {1, 2, 4, ..., 2**(x-1)}

def maguffinTotalPrice(maguffinPrice, n):
  return sum([maguffinPrice(i)+1 for i in range(n+1)])

def maguffinPurchase3(total_money, maguffinPrice):
  n = 0
  while maguffinTotalPrice(maguffinPrice, n) <= total_money:
      n += 1
  return n

# Test cases with input value of 1000 (dictionary mapping):
results = dict.fromkeys(range(num_calls))
results[0] = maguffinPurchase3(1000, maguffinPrice_1)
results[1] = maguffinPurchase3(1000, maguffinPrice_2)
print('Item 2c):')
print(results[0])  # Output: 44
print(results[1],'\n')  # Output: 9

# Using the maguffinTotalPrice lambda functions, as an illustration outside
# the requested scope of the task:
def maguffinPurchase4(total_money, maguffinTotalPrice):
  n = 0
  while maguffinTotalPrice(n + 1) <= total_money:
      n += 1
  return n

# Test cases with input value of 1000:
print('Outside the scope of task:')
print(maguffinPurchase4(1000, maguffinTotalPrice_1))  # Output: 44
print(maguffinPurchase4(1000, maguffinTotalPrice_2))  # Output: 9