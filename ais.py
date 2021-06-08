import pandas as pd
Name=['RAM','james','sam','peter']
S=pd.Series([20,30,52,10],index=Name)
S1=pd.Series([17,13,32,21],index=Name)
print(S.index,S.values)
print(S[0:2])
