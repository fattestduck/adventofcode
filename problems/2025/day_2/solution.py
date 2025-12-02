import argparse
import re
import numpy as np

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall(r'[-+]?\d+', string)))
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.ranges = [tuple(map(int, item.split("-"))) for item in self.file.split(",")]
  
  @staticmethod
  def is_invalid(num: str, chunk_sizes: list[int]):
    num = str(num)
    for chunk_size in chunk_sizes:
      sub_nums = [num[i:i+chunk_size] for i in range(0, len(num), chunk_size)]
      if len(np.unique(sub_nums)) == 1:
        return True
    return False
    
  def part1(self):
    invalid_ids = []
    for start, end in self.ranges:
      for num in range(start, end+1):
        if self.is_invalid(num, chunk_sizes=[len(str(num))//2]):
          invalid_ids.append(num)
    return sum(invalid_ids)
  
  def part2(self):
    invalid_ids = []
    for start, end in self.ranges:
      for num in range(start, end+1):
        chunk_sizes = list(range(1,len(str(num))//2 +1))
        if self.is_invalid(num, chunk_sizes=chunk_sizes):
          invalid_ids.append(num)
    return sum(invalid_ids)
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
