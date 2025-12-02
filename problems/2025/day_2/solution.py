import argparse
import re

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    ranges = string.split(',')
    return [tuple(s.split('-')) for s in ranges]

  @staticmethod
  def check_validity(id) -> bool:
    strid = str(id)
    build = ""
    #print(strid)
    for n in range(len(strid)):
      build += strid[n]
      #print (build)
      #print (strid[n+1:])
      #print (build == strid[n+1:])
      if build == strid[n+1:]:
        return False
      

    #raise Exception
    return True

  '''
  1: obtain the first digit
  2: check if the remainder is simply that digit repeating
  3: if not, obtain the next digit and append to the first
  4: check if the remainder is simply that new build repeating
  5: repeat until either a match is found or the build is the entire number
  6: if the build is the entire number, return True
  7: if a match is found, return False
  
  '''
  def check_validity2(self, id) -> bool:
    strid = str(id)
    build = ""
    #print(strid)
    for n in range(len(strid)):
      build += strid[n]
      remainder = strid[n+1:]
      if build == remainder:
        return False
      else:
        chunks = [remainder[i:i+len(build)] for i in range(0, len(remainder), len(build))]
        #print(chunks)
        sc = set(chunks)
        if len(sc) == 1 and build in sc:
          return False

    return True
    
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.lines = self.file.splitlines()
    
  def part1(self):
    ranges = self.get_nums(self.file)
    invalids = []

    for r in ranges:
      ids = range(int(r[0]), int(r[1])+1)
      for id in ids:
        if (self.check_validity(id) == False):
          invalids.append(id)

    print(f'Invalid IDs: {invalids}')
    return sum(invalids)
  
  def part2(self):
    ranges = self.get_nums(self.file)
    invalids = []

    for r in ranges:
      ids = range(int(r[0]), int(r[1])+1)
      for id in ids:
        if (self.check_validity2(id) == False):
          invalids.append(id)
    print(f'Invalid IDs: {invalids}')
    return sum(invalids)
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
