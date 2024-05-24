#!/usr/bin/env python3

import os.path
import sys

def main():
  root_dir = sys.argv[1]
  for path, _, file_lst in os.walk(root_dir):
    rel_path = ''
    if path != root_dir:
      rel_path = os.path.relpath(path, root_dir)

    for file in file_lst:
      print(f'"{os.path.join(rel_path, file)}",')

  return 0

if __name__ == '__main__':
  sys.exit(main())
