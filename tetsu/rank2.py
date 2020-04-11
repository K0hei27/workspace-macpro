import pandas as pd

df = pd.read_csv('./data.csv',sep=' ')
df_s = df.sort_values('SCORE',ascending=False)
l = df_s.reset_index()

user_id = input("Input your user ID : ")
user_score = int(input("Your Score : "))

num = 0
total = len(l)
while l.loc[num,'SCORE'] > user_score:
    num += 1
else:
    print('Your ID : {}'.format(user_id))
    print('Your Rank : {0} / {1}'.format(num, total))
    if num/total <0.1:
        print('Perfect!!')
    elif num/total < 0.2:
        print('Great:)')
    elif num/total < 0.4:
        print('Good:)')
    else:
        print("Let's do our best next time!")
