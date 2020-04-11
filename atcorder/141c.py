N, K, Q  = map(int, input().split())
win_list = [int(input()) for i in range(Q)]
score = [K for i in range(N)]

for x in win_list:
    for a, b in enumerate(score):
        if not a == x-1:
            score[a] = b-1
            
for s in score:
    if s > 0:
        print('Yes')
    else:
        print('No')
