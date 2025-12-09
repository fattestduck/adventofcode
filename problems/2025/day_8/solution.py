import argparse
import re
import math
import numpy as np

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall(r'[-+]?\d+', string)))
  
  # @staticmethod
  # def dist(p: tuple, q: tuple) -> float:
  #   return math.dist(p, q)


  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.lines = self.file.splitlines()
    
  def part1(self):
    coords = []
    for line in self.lines:
      coords.append(tuple([int(num) for num in line.split(',')]))
   #print(pts)

    n = len(self.lines)
    m = n * (n - 1) // 2  # 499,500 edges

    u = np.empty(m, dtype=np.int32)
    v = np.empty(m, dtype=np.int32)
    dists = np.empty(m, dtype=np.float64)

    # Build edges + distances
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            u[k] = i
            v[k] = j
            dists[k] = math.dist(coords[i], coords[j])
            k += 1

    # Sort edges by distance
    order = np.argsort(dists)
    dists_sorted = dists[order]
    u_sorted = u[order]
    v_sorted = v[order]

    # Now edges are sorted by distance increasing
    #print("Closest edge:")
    #print(dists_sorted[0], coords[u_sorted[0]], coords[v_sorted[0]])

    #shortest = dists_sorted[:10]
    
    circuits = []
    to_check = n

    for d in range(to_check):
      a = coords[u_sorted[d]]
      b = coords[v_sorted[d]]
      #print(a, b)
      found = False

      newcirc = set([a,b])
      for i, c in enumerate(circuits):
        if a in c or b in c:
          # print("matched")
          # print(newcirc)
          # print(c)
          newcirc = newcirc | c
          circuits.pop(i)
          found = True
      circuits.append(newcirc)
#    for c in circuits:
      #print(len(c))
  
    circuits.sort(key=len, reverse=True)
    
    #print(circuits[:3])
    #print(circuits)
    return math.prod(len(x) for x in circuits[:3])

  def part2(self):
    coords = []
    for line in self.lines:
      coords.append(tuple([int(num) for num in line.split(',')]))
   #print(pts)

    n = len(self.lines)
    m = n * (n - 1) // 2  # 499,500 edges

    u = np.empty(m, dtype=np.int32)
    v = np.empty(m, dtype=np.int32)
    dists = np.empty(m, dtype=np.float64)

    # Build edges + distances
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            u[k] = i
            v[k] = j
            dists[k] = math.dist(coords[i], coords[j])
            k += 1

    # Sort edges by distance
    order = np.argsort(dists)
    dists_sorted = dists[order]
    u_sorted = u[order]
    v_sorted = v[order]

    # Now edges are sorted by distance increasing
    #print("Closest edge:")
    #print(dists_sorted[0], coords[u_sorted[0]], coords[v_sorted[0]])

    #shortest = dists_sorted[:10]
    
    circuits = []
    to_check = n

    #for d in range(to_check):
    #print(dists_sorted)
    for d, dist in enumerate(dists_sorted):
      a = coords[u_sorted[d]]
      b = coords[v_sorted[d]]
      #print(a, b)
      
      found = False

      matches = []
      for i, c in enumerate(circuits):
        if a in c or b in c:
          matches.append(i)

      if len(matches) == 0:
        circuits.append(set([a,b]))
      else:
        newcirc = set([a,b])
        for m in matches:
          newcirc = newcirc | circuits[m]
        
        newcircs = [element for index, element in enumerate(circuits) if index not in matches]
        newcircs.append(newcirc)
        circuits = newcircs

      circuits.sort(key=len, reverse=True)
      if len(circuits[0]) == n:
        return a[0]*b[0]
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
