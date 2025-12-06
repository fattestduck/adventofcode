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
    ranges = set()
    lines = []
    for line in self.lines:
      if line == '':
        break
      start, end = line.split('-')
      start = int(start)
      end = int(end)
      lines.append((start, end))

    slines = sorted(lines)
    sorted_lines = list(dict.fromkeys(slines))

    print(sorted_lines)
    #return
    fresh = set()

    highest = 0
    for x, rc in enumerate(sorted_lines):
      print("x: " + str(x))
      # if x != 0 and x <= y_tracker:
      #   print("skipping")
      #   continue

      start_c = rc[0]
      end_c = rc[1]
      print("currently testing: " + str(rc[0]) + "," +str(rc[1]))
      rng_start = start_c
      rng_end = end_c
      
      if rng_end <= highest:
        print("skipping")
        continue

      for y, rn in enumerate(sorted_lines[x+1:]):
        #print("y: " + str(y+x+1))
        #y_tracker = y+x+1
        start_n = rn[0]
        end_n = rn[1]

        if start_n > rng_end or end_n <= rng_end:
          continue
        else:
          rng_end = end_n


      print("adding:")
      print((rng_start, rng_end))
      fresh.add((rng_start, rng_end))
      highest = rng_end

    #print(sorted_lines)

    cum = 0
    print(fresh)
    for f in fresh:
      cum += f[1]-f[0]+1

    return cum



    

  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
