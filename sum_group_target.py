import itertools

def sum_group_target(list,length,target):
  results=[]
  for group in itertools.combinations(list, length):
    if sum(group)==target:
      results+=[group]
  print results
  
sum_group_target([2,5,6,33,88,10,22,49,10,1],3,42)