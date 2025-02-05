import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("movie.csv")

#写入数据库
conn = create_engine('mysql+pymysql://root:153517@localhost:3306/big_spider')
df.to_sql('movie', con=conn, if_exists='replace', index=False)

#柱状图，统计各个分数的影片数量
plt.figure(figsize=(20,8),dpi=100)
plt.hist(df["movie_score"].values,bins=12)
max_=df["movie_score"].max()
min_=df["movie_score"].min()
t1=np.linspace(min_,max_,num=13)
plt.xticks(t1)
plt.grid()
plt.xlabel("score")
plt.ylabel("count")
plt.show()