import random
import uuid
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

id = [str(uuid.uuid4())[:6] for i in range(100000)]
score = [np.random.normal(60,10) for i in range(100000)]
df = pd.DataFrame({'ID':id,'SCORE':score})
df.to_csv('data.csv',sep=' ',index=False)
plt.hist(score)
plt.show()
