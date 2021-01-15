#!/usr/bin/env python3
import sys

'''
def configure():
  current = os.path.dirname(os.path.realpath(__file__))
  print('Please pass json file directory.\nFor more information please visit https://github.com/a1eaiactaest/aclass')
'''

#TODO: Make function that takes argument from args and joins the lesson
def join(subject):
  import json
  import webbrowser
  f = open('classes.json','r')
  data = json.load(f)
  url = data[subject]
  webbrowser.open(url,new=0,autoraise=False)

def main():
  argument = sys.argv[1]
  if argument == '--configure':
    import os
    import urllib.request
    # download file from gh repo and open it in vi for user to edit it
    current = os.path.dirname(os.path.realpath(__file__))
    url = 'https://raw.githubusercontent.com/a1eaiactaest/aclass/master/docs/classes.json'
    urllib.request.urlretrieve(url, f'{current}/classes.json')
    os.system(f'vi {current}/classes.json')
    print('Configuration complete, running this procces again will overwrite existing data.')

  elif argument == '--join':
    # create second argument and take value from json file
    subject = sys.argv[2]
    join(subject)
  
  elif argument == '--help' or argument == '-h':
    help_message = '''
    usage: aclass [OPTION] {ARGUMENT}
    
    Join your classes.
    For usage and help visit: https://github.com/a1eaiactaest/aclass

    arguments:
    -h, --help      display this help
    --configure     configure aclass by writing file with your classes.
    --join {class}  join to your class. Passing object from classes.json file as argument.
    '''
    print(help_message)

  else:
    # print help
    pass

if __name__ == "__main__":
  main()
