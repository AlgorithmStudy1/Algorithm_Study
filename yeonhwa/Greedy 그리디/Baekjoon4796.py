'''
**Info**
	GitHub name : yhlee0
	Subject : Baekjoon 4796 캠핑
	URL : https://www.acmicpc.net/problem/4796
'''


cnt =1
while 1:
  L, P, V = map(int, input().split())
  if L == 0 and P == 0 and V == 0:
    break
  res = (V//P)*L
  res += min((V % P), L)
  print('Case %d: %d' % (cnt, res))
  cnt += 1
