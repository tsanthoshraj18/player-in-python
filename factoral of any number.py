def fac(number1):
  if number1==0:
    return 1
  else:
    return number1*fac(number1-1)
number1=int(input())
print(fac(number1)) 