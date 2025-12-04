import argparse
import re

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
    
  def is_roll(self, row: int, col: int) -> bool:
    if row < 0 or col < 0 or row >= len(self.lines) or col >= len(self.lines[0]):
      return False
    elif self.lines[row][col] == '@':
      return True
    else:
      return False
    
  def part1(self):
    rows = len(self.lines)
    cols = len(self.lines[0])
    #print("Rows: ", rows, " Cols: ", cols)
    count = 0
    for row in range(rows):
      print(self.lines[row])
      for col, value in enumerate(self.lines[row]):
        if value == '@':
          adj = 0
          # check all 8 directions
          for [dr, dc] in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
            r = row + dr
            c = col + dc
            if self.is_roll(r, c) == True:
              adj += 1
            if adj > 3:
              break
          if adj <= 3:
            #print("Valid roll at: ", row, col)
            count += 1
    return count
  
  def part2(self):
    rows = len(self.lines)
    cols = len(self.lines[0])
    cum = 0
    while True:
      count = 0
      for row in range(rows):
        for col, value in enumerate(self.lines[row]):
          if value == '@':
            adj = 0
            # check all 8 directions
            for [dr, dc] in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
              r = row + dr
              c = col + dc
              if self.is_roll(r, c) == True:
                adj += 1
              if adj > 3:
                break
            if adj <= 3:
              self.lines[row] = self.lines[row][:col] + '.' + self.lines[row][col+1:]
              count += 1
      cum += count
      if count == 0:
        return cum

  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
