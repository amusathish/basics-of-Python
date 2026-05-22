def unit_matrix(n):
  i = 0
  j = 0
  l = []
  for i in range(n):
    rows = []
    for j in range(n):      
      if(i == j):
        rows.append(1)
      else:
        rows.append(0)
    l.append(rows)   
  print(l)
  return(l)  

  