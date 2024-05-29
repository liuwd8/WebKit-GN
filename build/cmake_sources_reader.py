#!/usr/bin/env python3
import sys
import re
import argparse

comment_pattern = re.compile("//.*$", re.RegexFlag.M)
string_pattern = re.compile("@no-unify", re.RegexFlag.M)
space_pattern = re.compile("[^\S\n]", re.RegexFlag.M)
newline_pattern = re.compile("^\n", re.RegexFlag.M)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('files', nargs='+')
  args = parser.parse_args()

  lines = ""
  for f in args.files:
    with open(sys.argv[1], "r", ) as f:
      content = f.read()
      content = re.sub(comment_pattern, "", content)
      content = re.sub(string_pattern, "", content)
      content = re.sub(space_pattern, "", content)
      content = re.sub(newline_pattern, "", content)
      lines += content

  lines = re.sub(space_pattern, "", lines)
  lines = re.sub(newline_pattern, "", lines)
  print(lines)

if __name__ == '__main__':
  sys.exit(main())
