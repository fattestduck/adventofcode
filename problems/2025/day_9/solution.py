import argparse
import re
import math

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall(r'[-+]?\d+', string)))
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.lines = self.file.splitlines()
    
  def part1(self):
    #top left = (1659, 1739)
    #bottom right = (98432, 98352)
    #origin at top left

    pts = set()
    
    for line in self.lines:
      x, y = line.split(",")
      pts.add((int(x), int(y)))

    #area = LxH    L = (x2 - x1) +1  H = (y2 - y1) +1   

    winner = 0
    for p in pts:
      for q in pts:
        area = ( abs(q[0]-p[0])+1 ) * ( abs(q[1]-p[1])+1)
        if area > winner:
          winner = area

    return winner

    pass
  
  def add_between(self, p1, p2, greens) -> set:
    p1x = p1[0]
    p1y = p1[1]
    p2x = p2[0]
    p2y = p2[1]

    if p1x == p2x:  # vertical line
      if p1y > p2y: # bottom up
        for step in range(p1y-p2y):
          greens.add((p1x, p1y-step))
      else: # top down
        for step in range(p2y-p1y):
          greens.add((p1x, p1y+step))
    else: # horizontal line
      if p1x > p2x: #right to left
        for step in range(p1x-p2x):
          greens.add((p1x-step, p1y))
      else: # left to right
        for step in range(p1x-p2x):
          greens.add((p1x+step, p1y))

    return greens

  def part2(self):
    pts = []
    
    for line in self.lines:
      x, y = line.split(",")
      pts.append((int(x), int(y)))

    segs = set()
    reds = set()
    greens = set()
    for i in range(len(pts)):
      p = pts[i]
      reds.add(p)
      pn = pts[i+1] if i < len(pts) -1 else pts[0]
      pp = pts[i-1]

      greens = self.add_between(p, pn, greens)
      greens = self.add_between(p, pp, greens)

    # for y in range(10):
    #   ln = ""
    #   for x in range(14):
    #     tp = (x, y)
    #     if tp in reds:
    #       ln += '#'
    #     elif tp in greens:
    #       ln += 'X'
    #     else:
    #       ln += '.'
    #   print(ln)

    valids = reds | greens

    winner = 0
    for p in reds:
      for q in reds:
        valid = False
        area = ( abs(q[0]-p[0])+1 ) * ( abs(q[1]-p[1])+1)

        toplt = ( min(p[0], q[0]), min(p[1], q[1]) )
        toprt = ( max(p[0], q[0]), min(p[1], q[1]) )
        botlt = ( min(p[0], q[0]), max(p[1], q[1]) )
        botrt = ( max(p[0], q[0]), max(p[1], q[1]) )

        if toplt in valids and toprt in valids and botlt in valids and botrt in valids:
          valid = True

        if area > winner and valid == True:
          winner = area

    return winner

    pass
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
