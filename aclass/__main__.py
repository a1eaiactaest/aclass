#!/usr/bin/env python3

import os
import argparse

def main():
  parser = argparse.ArgumentParser(description='Automate you online classes')
  parser.add_argument('--configure', help='Add class URLs', action='store_true')
  parser.add_argument('--join', help='Add class URLs', action='store_true', default=argparse.SUPRESS)
  args = parser.parse_args()


  print(args)

if __name__ == "__main__":
  main()
