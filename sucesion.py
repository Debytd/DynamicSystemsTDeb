def suc(N):
  s = []
  ss = []
  for i in range(N):
    s.append(1/10**i)
    ss.append('\\frac\{1}{10^{' + str(i) +'}}')
  print(ss)
  print(s)
  
  suc(int(input()))
