def shrink_string_iterative(s):
  counter=1
  cycle=0
  len_s=0
  flag=True
  print s,len(s)
  while flag:
    len_s=len(s)
    for i in xrange(len(s)-1):
      for j in xrange(i+1,len(s)):
        print i,s[i],j,s[j],counter,'length of string is {0}'.format(len(s)),len_s,cycle
        if s[i]==s[j]:
          counter+=1
          if j==len(s)-1:
            if counter>=3:
              counter=1
              print s[:i],s[j:]
              s=s[:i]
              print s,len(s)
              break
            else:
              counter=1
              break
        elif counter>=3:
          counter=1
          print s[:i],s[j:]
          s=s[:i]+s[j:]
          print s,len(s)
          break
        else:
          counter=1
          break
    if len_s==len(s):
      cycle+=1
    if cycle==2:
      flag=False
  print s
shrink_string_iterative('abaabbaaab')

def shrink_string_recursive(string):
  flag=False
  j=0
  for i in xrange(len(string)-1):
    while string[i]==string[i+j] and j+i!=len(string)-1:
      j+=1
    if j>=3:
      if j+i==len(string)-1:
        print string[:i]
        string=string[:i]
      else:
        print string[:i],string[j+i:]
        string=string[:i]+string[j+i:]
      flag=True
      break
    else:
      j=0
  if flag:
    shrink_string_recursive(string)
  else:
    print string
    
shrink_string_recursive('aaaaabcccccdeeeffffgggg')
