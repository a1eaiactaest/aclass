#!/usr/bin/env python3
import sys

'''
def configure():
  current = os.path.dirname(os.path.realpath(__file__))
  print('Please pass json file directory.\nFor more information please visit https://github.com/a1eaiactaest/aclass')
'''

#TODO: Make function that takes argument from args and joins the lesson
def join(subject):
  pass

def main():
  argument = sys.argv[1]
  if argument == '--configure':
    import os
    import urllib.request
    #configure()
    current = os.path.dirname(os.path.realpath(__file__))
    url = 'https://raw.githubusercontent.com/a1eaiactaest/aclass/master/docs/classes.json'
    urllib.request.urlretrieve(url, f'{current}/classes.json')
    os.system(f'vi {current}/classes.json')
    print('Configuration complete, running this procces again will overwrite existing data.')

  elif argument == '--join':
    # create second argument and take value from json file
    subject = sys.argv[2]
    join(subject)
  else:
    # print help
    pass

if __name__ == "__main__":
  main()
