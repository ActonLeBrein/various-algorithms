def longest_zero_list_binary(integer):
  max_zero=[0]*3
  integer='{0:b}'.format(integer)
  int_list=integer.split('1')
  for i in xrange(len(int_list)):
    if len(int_list[i])>max_zero[0]:
      max_zero=[len(int_list[i]),i+len(int_list[i]),int_list[i]]
  print 'the longest list of zeros is {0} {2} at position {1} in {3}'.format(max_zero[0],max_zero[1],max_zero[2],integer)
  
longest_zero_list_binary(1250)