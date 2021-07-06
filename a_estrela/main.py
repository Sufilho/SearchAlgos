import numpy as np

a = np.array([[0,0,0], [0,0,0], [0,0,0]])

def getRandCoord(arr):
  """
    Only for bidimensional arrays
  """
  if len(arr.shape) > 2:
    return
  
  rand_i = np.random.randint(0, arr.shape[0])
  rand_j = np.random.randint(0, arr.shape[1])

  return [rand_i, rand_j]

def getStartEnd(randCoord, arr):
  start = randCoord(arr)
  end = randCoord(arr)
# for x in range(100):
#   print(np.random.randint(0, a.shape[1]))
print(a)
ini_coord = getRandCoord(a)
fin_coord = getRandCoord(a)
a[ini_coord[0]][ini_coord[1]] = 1
print(a)

# for x in range(10):
#   rand_coord = getRandCoord(a)
#   print(a[rand_coord[0]][rand_coord[1]], '->', rand_coord[0], rand_coord[1])
