#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batchdict = {}
  for i in recipe:
    batchdict[i] = 0
  print(batchdict)
  
  
  if len(recipe) > len(ingredients):
    return 0
  else:
    enough = True
    while enough:
      for i in recipe:
        if recipe[i] < ingredients[i]:
          batchdict[i]+=1
          ingredients[i] -= recipe[i]
        else:
          enough = False
    print("2", batchdict)
    batcharr = list(batchdict.values())
    return min(batcharr)

print(recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 }))
  


# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))