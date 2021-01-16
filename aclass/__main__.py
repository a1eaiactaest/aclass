#!/usr/bin/env python3
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))

def join(subject, data):
  import json
  import webbrowser
  url = data[subject]
  webbrowser.open(url,new=0,autoraise=False)
 
def helpm():
    help_message = '''
    usage: aclass [OPTION] {ARGUMENT}
    
    Join your classes.
    For usage and help visit: https://github.com/a1eaiactaest/aclass

    arguments:
    -h, --help      display this help
    --configure     configure aclass by writing file with your classes.
    --join {class}  join to your class. Passing object from classes.json file as argument.
    --edit          edit classes.json file, it contains links to your online classes
    '''
    print(help_message)

def main():
  argument = sys.argv[1]
  if argument == '--configure':
    import urllib.request
    # download file from gh repo and open it in vi for user to edit it
    url = 'https://raw.githubusercontent.com/a1eaiactaest/aclass/master/docs/classes.json'
    urllib.request.urlretrieve(url, f'{current}/classes.json')
    os.system(f'vi {current}/classes.json')
    print('Configuration complete, running this procces again will overwrite existing data. Run --edit to edit this file again.')

  if argument == '--join':
    # create second argument and take value from json file
    import json
    key = sys.argv[2]
    data = json.load(open(f'{current}/classes.json', 'r'))
    if key in data:
      join(key, data)
    else:
      helpm()
 
  if argument == '--edit':
    # basically works same as --configure but doesnt fetch classes.json from repo
    os.system(f'vi {current}/classes.json')
    print(f'Your classes.json file is {current} directory')

  if argument == '--help' or argument == '-h':
    helpm()

if __name__ == "__main__":
  main()
