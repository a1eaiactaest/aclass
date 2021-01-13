#!/usr/bin/env python3

import os
import argparse


#TODO: Make function that takes argument from args and joins the lesson
def join():
  pass

def main():
  parser = argparse.ArgumentParser(description='Automate you online classes')
  parser.add_argument('--configure', help='Add class URLs', action='store_true')
  parser.add_argument('--join', help='Add class URLs', default=argparse.SUPPRESS)
  args = parser.parse_args()


  print(args.join)

if __name__ == "__main__":
  main()
