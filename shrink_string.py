def shrink_string(s):
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
shrink_string('abaabbaaab')