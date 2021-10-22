n = list(map(int, (input("Enter List : ").split())))
ls,tmp = [],[]
i = 0
# while i < len(n)-1:
  if len(tmp) == 0:
    tmp.append(n[i])
  if n[i] == 1 and n[i-1]-1 != 1:
    ls.append(tmp)
  if tmp[-1]-n[i+1] == 1:
    tmp.extend([n[i+1]])
    if n[i+1] == 1:
      ls.append(tmp)
      tmp = []
  else:
    tmp=[]
  i += 1
result = [len(ls)]
result.append(ls)
print(result)
