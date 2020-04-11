S = input()
Sl = list(S)
o = Sl[0::2]
e = Sl[1::2]

if 'R' in e or 'L' in o:
    print('No')
else:
    print('Yes')
