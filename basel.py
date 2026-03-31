Write a function called basel which returns an approximation of the Basel sum:


the sum has infinitely many terms but it eventually converges to π2/6. Your function should take a parameter epsilon and sum as many terms as possible until the next one is less than epsilon.

Note that we don't know in advance how many terms to sum, instead we have a termination condition. This indicates that it is convenient to use a while loop.

--------------------------------------------

def basel(epsilon):
  s = 0
  n = 1
  while ((1/n**2) > epsilon ):
    s = s + (1/n**2 )
    n += 1
    print(f"s= {s} , n={n}")
  return s

basel(0.5)
basel(5e-05)