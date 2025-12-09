import argparse
import re
import functools
from collections import defaultdict
from treelib import Tree

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  tree = {}
  
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
    self.tree = defaultdict(list)
    #tree = Tree()

    count = 0
    for row, line in enumerate(matrix):
      if row == 0:
        pos = line.find('S')
        newline = line.replace('S','|')
        matrix[row] = newline
        root = (row, pos)
        print(root)
        self.tree[(root)] = []
        #tree.create_node(root, root)
        continue
      tachs = set()
      splits = set()
      for col, char in enumerate(line):
        if matrix[row-1][col] == '|':
          if char == '^':
            tachs.add(col-1)
            tachs.add(col+1)
            splits.add(col)
            #count += 1
            newline = line[:col-1] + '|^|' + line[col+2:]

            prev = (row-1, col)
            left = (row, col-1)
            right = (row, col+1)

            # if left in tree:
            #   count += 1
            # else:
            #   tree.create_node(left, left, parent=prev)
            # if right in tree:
            #   count += 1
            # else:
            #   tree.create_node(right, right, parent=prev)

            prev_node = self.tree[(row-1, col)]
            left_node = self.tree[(row, col-1)]
            right_node = self.tree[(row, col+1)]
            prev_node.append((row, col-1))
            prev_node.append((row, col+1))
            self.tree[(row-1, col)] = prev_node

          elif char == '.':
            #node = Node((row, col))
            newline = line[:col] + '|' + line[col+1:]
            prev_node = self.tree[(row-1, col)]
           # print(prev_node)
            new_node = self.tree[(row, col)]
            prev_node.append((row, col))
            self.tree[(row-1, col)] = prev_node
            tachs.add(col)
            prev = (row-1, col)
            down = (row, col)
            # if down not in tree:
            #   tree.create_node(down, down, parent=prev)
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

    root_node = (0, 70)
    paths = self.count_paths_to_leaves(root_node)
    return paths

    # realtree = Tree()
    # root = (0,7)
    # realtree.create_node(root, root)
    # for parent, children in tree.items():
    #   #print(parent)
    #   #print("children:")
    #   #print(children)
    #   for child in children:
    #     #print("child:")
        
        # realtree.create_node(child, child, parent=parent)

    # #realtree.show()
    # leaves = tree.leaves()
    # leaf_paths = tree.paths_to_leaves()
    # #print(leaves)
    # print(count)
    # print(len(leaf_paths))
    # #return len(leaves) + count
  
  @functools.lru_cache(maxsize=None)
  def count_paths_to_leaves(self, node):
    if not self.tree[node]:
      return 1
    
    total_paths = 0
    for neighbor in self.tree[node]:
      total_paths += self.count_paths_to_leaves(neighbor)

    return total_paths

if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
