import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("movie.csv")

#科幻片数量
df_science=df[[i.find("幻")!=-1 for i in df['movie_type']]]
science=df_science["movie_type"].count()

#爱情片数量
df_love=df[[i.find("爱情")!=-1 for i in df['movie_type']]]
love=df_love["movie_type"].count()

#动作片数量
df_action=df[[i.find("动作")!=-1 for i in df['movie_type']]]
action=df_action["movie_type"].count()

#动画片数量
df_carton=df[[i.find("动画")!=-1 for i in df['movie_type']]]
carton=df_carton["movie_type"].count()

#惊悚片数量
df_thriller=df[[i.find("惊悚")!=-1 for i in df['movie_type']]]
thriller=df_thriller["movie_type"].count()

#喜剧片数量
df_drama=df[[i.find("喜剧")!=-1 for i in df['movie_type']]]
drama=df_drama["movie_type"].count()

# 饼图
slices=[science,love,action,carton,thriller,drama]
label=['science','love','action','carton','thriller','drama']
cols=['blue','red','green','pink','orange','yellow']
plt.pie(slices,labels=label,colors=cols,startangle=90,autopct='%1.1f%%')
plt.show()