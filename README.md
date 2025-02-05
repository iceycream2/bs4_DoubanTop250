# 豆瓣电影Top250数据分析与可视化

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)

本项目为本人大二学习数据处理，通过python爬取豆瓣电影Top250数据，进行数据清洗、分析、可视化，并实现数据持久化存储，完整展示了数据处理的典型流程。

## 项目概述
- 🕷️ 使用Requests+BeautifulSoup实现高效网页爬取
- 📊 使用Pandas进行数据清洗与分析
- 📈 使用Matplotlib生成可视化图表
- ☁️ 使用使用jieba库进行分词WordCloud创建词云图
- 🗄️ 使用SQLlalchemy实现MySQL数据库存储

## 技术栈
- **爬虫框架**：Requests + BeautifulSoup
- **数据分析**：Pandas + NumPy
- **数据可视化**：Matplotlib + Seaborn + WordCloud
- **数据库**：MySQL + PyMySQL
- **开发环境**：Python 3.10、VS Code

## 功能实现
### 1. 数据爬取模块
- 实现自动翻页抓取（处理25页分页逻辑）
- 字段解析：
  - 电影名称
  - 评分/评价人数（数值类型转换）
  - 电影分类（标签解析）
- 反爬策略：
  - User-Agent
  - 请求间隔控制

### 2. 数据处理模块
- 数据清洗：
  - 处理缺失值
  - 规范日期格式
  - 类型标签标准化
- 数据存储：
  - CSV临时存储
  - Mysql持久化存储

### 3. 可视化模块
- 评分分布直方图（Matplotlib）
- 电影类型占比饼图（Matplotlib）
- 类型关键词词云（jieba分词）

### 4. 未来改进
- 添加Docker支持
- 实现定时自动更新数据
- 构建Flask/Dash可视化仪表盘
- 增加ElasticSearch全文搜索功能
