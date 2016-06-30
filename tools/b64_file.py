# coding: utf-8

def read_file(in_path):
  with open(in_path,'r') as f:
    return(f.read())

def b64_file(in_path):
  from base64 import b64encode as b64
  return(b64(read_file(in_path).encode('utf-8')))

if __name__ == '__main__':
  print(b64_file(input('enter the file path: ')))
