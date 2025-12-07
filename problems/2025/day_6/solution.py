import argparse
import math
import re
import numpy as np
import itertools

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
    #self.lines.pop()
    #arr = np.array([list(row) for row in self.lines]).transpose()
    #print(arr)
    #return
    #z = zip(self.lines)
    #print(list(z))
    # self.lines.pop()

    # z = [list(nums) for blank, nums in itertools.groupby([''.join(row).strip() for row in zip(*self.lines)], bool) if blank]

    # #z = zip(*self.file.splitlines())
    # print(list(z))

    #matrix = [line.split() for line in self.lines]
    #transposed = list(zip(*matrix[::-1]))
    #print(transposed)

    #z = zip([list(row.split()) for row in self.lines])
    #print (list(z))
    #z = zip(self.file.split())
    #print (list(z))
    # return


    operators = self.lines.pop().replace(" ","")

    cum = 0
    #print(operators)
    problems = []

    for line in self.lines:
      number_strs = line.split()
      numbers = [int(s) for s in number_strs]
      problems.append(numbers)

    matrix = np.array(problems)
    
    for pid, operator in enumerate(operators):
      col = matrix[:, pid]

      result = 0
      if operator == '*':
        result = math.prod(col)
      elif operator == '+':
        result = sum(col)

      cum += result

    return cum
    pass
  
  def part2(self):
    operators = self.lines.pop().replace(" ","")
    cum = 0
    result = 0
    str_matrix = []
    for line in self.lines:
      str_matrix.append(list(line))
    matrix = np.array(str_matrix)

    n = len(self.lines[0])-1
    for operator in reversed(operators):
      print("operator: " + operator)
      result = 0
      while True:
        if n < 0:
          break
        col = matrix[:,n]
        num_str = ""
        for c in col:
          if c != ' ':
            num_str += c

        if num_str == '':
          n = n - 1
          break
        else:
          num = int(num_str)
          print("doing num " + str(num))
          if operator == '*':
            if result == 0:
              result = num
            else:
              result = result * num
          elif operator == '+':
            result = result + num
        n = n - 1
      print("found result: " + str(result))
      cum += result
    return cum


    

    pass
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
