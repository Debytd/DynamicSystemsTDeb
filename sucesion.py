def suc(N):
  s = []
  ss = []
  for i in range(N):
    s.append(1/10**(i+1))
    ss.append('\\frac\{1}{10^{' + str(i+1) +'}}')
  print(ss)
  print(s)
  
  suc(int(input()))
