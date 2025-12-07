import argparse
import re
import functools
from collections import defaultdict
from treelib import Tree

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
    matrix = self.lines.copy()
    count = 0
    for row, line in enumerate(matrix):
      if row == 0:
        newline = line.replace('S','|')
        matrix[row] = newline
        continue
      tachs = set()
      splits = set()
      for col, char in enumerate(line):
        if matrix[row-1][col] == '|':
          if char == '^':
            tachs.add(col-1)
            tachs.add(col+1)
            splits.add(col)
            count += 1
            #newline = line[:col-1] + '|^|' + line[col+2:]
          elif char == '.':
            #newline = line[:col] + '|' + line[col+1:]
            tachs.add(col)
      newline = ""
      for c in range(len(line)):
        if c in tachs:
          newline += "|"
        elif c in splits:
          newline += "^"
        else:
          newline += '.'

      matrix[row] = newline

    for r, l in enumerate(matrix):
      print(l)
    return count
    pass

  def part2(self):
    matrix = self.lines.copy()
    tree = defaultdict(list)


    count = 0
    for row, line in enumerate(matrix):
      if row == 0:
        pos = line.find('S')
        newline = line.replace('S','|')
        matrix[row] = newline
        #root = Node((0, pos))
        tree[(row, pos)] = []
        continue
      tachs = set()
      splits = set()
      for col, char in enumerate(line):
        if matrix[row-1][col] == '|':
          if char == '^':
            tachs.add(col-1)
            tachs.add(col+1)
            splits.add(col)
            count += 1
            #newline = line[:col-1] + '|^|' + line[col+2:]

            prev_node = tree[(row-1, col)]
            left_node = tree[(row, col-1)]
            right_node = tree[(row, col+1)]
            prev_node.append((row, col-1))
            prev_node.append((row, col+1))
            tree[(row-1, col)] = prev_node

          elif char == '.':
            #node = Node((row, col))
            #newline = line[:col] + '|' + line[col+1:]
            prev_node = tree[(row-1, col)]
           # print(prev_node)
            new_node = tree[(row, col)]
            prev_node.append((row, col))
            tree[(row-1, col)] = prev_node
            tachs.add(col)
      newline = ""
      for c in range(len(line)):
        if c in tachs:
          newline += "|"
        elif c in splits:
          newline += "^"
        else:
          newline += '.'

      matrix[row] = newline

    for r, l in enumerate(matrix):
      print(l)
    #print(tree)

    realtree = Tree()
    root = (0,7)
    realtree.create_node(root, root)
    for parent, children in tree.items():
      #print(parent)
      #print("children:")
      #print(children)
      for child in children:
        #print("child:")
        
        realtree.create_node(child, child, parent=parent)

    #realtree.show()
    leaves = realtree.leaves()
    print(leaves)
    return len(leaves)

  
  
  # @functools.lru_cache(maxsize=None)
  # def count_paths(self, current_node, target_node):
  #   if current_node == target_node:
  #     return 1

  #   count = 0
  #   for neighbor in self.tree.get(current_node, []):
  #     count += self.count_paths(neighbor, target_node)

if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
