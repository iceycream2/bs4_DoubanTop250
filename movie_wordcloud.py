import pandas as pd
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取CSV文件
df = pd.read_csv('movie.csv')

all_comments = ' '.join(df['movie_type'].dropna())

# 使用jieba进行中文分词
seg_list = jieba.cut(all_comments, cut_all=False)
seg_text = ' '.join(seg_list)

# 创建词云对象
wordcloud = WordCloud(
    width=350, height=350,
    background_color='white',  # 背景颜色
    max_words=200,             # 最大显示的词数
    font_path='simhei.ttf',    # 字体路径，以支持中文
    min_font_size=10,          # 最小字号
    max_font_size=100,         # 最大字号
    collocations=False
).generate(seg_text)

# 显示生成的词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # 不显示坐标轴
plt.show()