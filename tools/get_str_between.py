# coding: utf-8
def get_str_between(s, before, after):
  # returns an array of substrings between "before" and "after"
  # by: Cody Kochmann
  unique="~~~~this~is~the~obvious~way~to~do~it~~~~"
  second_unique="~~~~i~think~you'll~like~this~~~~~"
  s=(s.replace(before, unique).replace(after, second_unique).split(unique))
  out=[]
  while len(s)>0:
    tmp=s.pop()
    if second_unique in tmp:
      out.append(tmp.split(second_unique)[0])
  return(out)

if __name__ == '__main__':
	print(get_str_between('hello world','el','ld'))
