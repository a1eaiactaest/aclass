#!/usr/bin/env python3

import os
import argparse
import time 

def configure():
  current = os.path.dirname(os.path.realpath(__file__))
  f = open("classes.json", "w+")
  f.write('{\n\t"classes":{\n\n\t}\n}')
  f.close()
  os.system('vim classes.json') 
  time.sleep(10)

#TODO: Make function that takes argument from args and joins the lesson
def join():
  with open('classes.json', 'r') as class_data:
    print('opened')

def main():
  parser = argparse.ArgumentParser(description='Automate you online classes')
  parser.add_argument('--configure', help='Add class URLs', action='store_true')
  parser.add_argument('--join', help='Join your classes', default=argparse.SUPPRESS)
  parser.add_argument('--add', help='', action='store_true')
  args = parser.parse_args()
  

  if args.configure:
    configure()
  if args.join:
    join()

if __name__ == "__main__":
  main()
