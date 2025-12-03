import argparse
import re
import itertools

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall(r'\d', string)))
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.lines = self.file.splitlines()
    
  def part1(self):
    cum = 0
    for line in self.lines:
      #print(line)
      winner = 0
      for n in range(len(line)-1):
        tens = int(line[n])
        ones = max(self.get_nums(line[n+1:]))
        #print("Tens: ", tens, " Ones: ", ones)
        joltage = 10*tens + ones
        #print("Testing joltage: ", joltage)
        if joltage > winner:
          winner = joltage
      #print("Winner for line: ", winner)
      cum += winner

    return cum
  
  def strmax(self, string: str) -> int:
    nums = self.get_nums(string)
    #print(nums)
    return nums.index(max(nums))
    
  def part2(self):
    cum = 0
    for line in self.lines:
      build = ""
      remaining = 12
      index = 0
      while (remaining > 0):
        search = line[index:len(line)-remaining+1]
        #print(search)
        maxindex = self.strmax(search)
        build += line[index + maxindex]
        index += maxindex + 1
        remaining -= 1

      cum += int(build)

    return cum
    pass
  
  def part2_old(self):
    ll = len(self.lines[0])
    patterns = [''.join('0' if i in combo else '1' for i in range(ll)) for combo in itertools.combinations(range(ll), ll-12)]
    cum = 0

    for line in self.lines:
      winner = 0
      for pattern in patterns:
        joltage_str = ""
        for pindex in range(len(pattern)):
          if pattern[pindex] == '1':
            joltage_str += line[pindex]
        if int(joltage_str) > winner:
          winner = int(joltage_str)
      cum += winner


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
