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
    
  def test_num(self, num: int, ranges: set) -> bool:
    for r in ranges:
      if num >= r[0] and num <= r[1]:
        return True
    return False

  def part1(self):
    ranges = set()
    marker = False
    fresh = 0
    for line in self.lines:
      if marker == False and line == '':
        marker = True
        continue
      if marker == False:
        start, end = line.split('-')
        ranges.add((int(start), int(end)))
        #start = int(start)
        #end = int(end)
        #rng = range(start, end+1)
        #for n in rng:
          #ranges.add(n)
      else:
       # print(ranges)
        num = int(line)
       # print(num)
        if self.test_num(num, ranges) == True:
          fresh += 1
        #  print("Invalid number: ", num)
          #return num  
    return fresh
    pass
  
  def part2(self):
    fresh = set()
    for line in self.lines:
      if line == '':
        break
      start, end = line.split('-')
      rng = range(int(start), int(end)+1)
      for n in rng:
        fresh.add(n)
    return len(fresh)
    pass
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
