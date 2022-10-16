import glob
import os
import urllib.parse

parentfilename = 'parent'

def main():
  for dirname in glob.glob('./'+ parentfilename +'/*'):
    find_file(dirname)

def find_file(pathname):
  if os.path.isdir(pathname):
    for name in glob.glob(pathname + '/*'):
      find_file(name)
  elif os.path.isfile(pathname):
    # Processing "change file name" 
    decode = urllib.parse.unquote(pathname)
    os.rename(pathname, decode)
    # Processing
    if not os.path.exists(decode):
      print('path not exist')
      return
  else:
    print("It is a special file (socket, FIFO, device file)" )
  print()
    
main()