import time
import os

LAMPS = ['''
      .
 .    |    ,
  \   '   /
   ` ,-. '
--- (   ) ---
     \ /
    _|=|_
   |_____|
''',
         '''


         
     ,-.
    (   )
     \ /
    _|=|_
   |_____|
''']


def run():
    toggler = 0
    while True:
        os.system('cls')
        print(LAMPS[toggler])
        if toggler == 0:
            toggler += 1
        else:
            toggler -= 1
        time.sleep(0.5)


if __name__ == '__main__':
    run()
