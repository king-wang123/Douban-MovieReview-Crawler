import jieba
import jieba.analyse
from wordcloud import WordCloud
import matplotlib.pyplot as plt

class MovieReviewStatistic:
    def __init__(self, movie_name, comments_dict):
        self.movie_name = movie_name
        self.comments_dict = comments_dict
        self.length = len(comments_dict)
        self.stars_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0} # 初始化一个字典来存储每个星级的评论数量
        # 读取文件中的停用词列表
        with open('./data/stopwords.txt', 'r', encoding='utf-8') as file:
            self.stopwords = set(file.read().splitlines())
    
    def stastic_star(self):
        all_star = 0
        all_val = 0

        # 遍历comments_dict中的所有评论
        for comment in self.comments_dict:
            # 将星级转换为整数
            stars = int(comment['stars'])
            upvote = int(comment['upvote'])
            if stars == 0:
                continue
            # 增加对应星级的计数
            self.stars_count[stars] += 1
            all_star += stars * upvote
            all_val += 5 * upvote

        # 打印每个星级的评论数量
        for star in sorted(self.stars_count.keys()):
            print(f"星级 {star} 的评论数量: {self.stars_count[star]}")
            
        star_avg = all_star / all_val
        star_avg = star_avg * 5
        print(f"点赞加权的平均星级: {star_avg:.2f}")

    def statistic_comment(self):
        # 初始化一个空列表来存储处理后的文本
        processed_strings = []

        # 预处理每个评论内容，并将其添加到processed_strings列表中
        for comment in self.comments_dict:
            # 提取关键词并用空格连接
            keywords = ' '.join(jieba.analyse.extract_tags(comment['content'], topK=20, withWeight=False))
            # 将处理后的文本添加到列表中
            processed_strings.append(keywords)

        # 将所有处理后的文本连接成一个单独的字符串
        string = ' '.join(font for font in processed_strings if font not in self.stopwords)

        # 创建词云对象，并生成词云
        wc = WordCloud(
            background_color='white',
            width=1000,
            height=800,
            font_path = r'C:\Windows\Fonts\SIMSUN.TTC',  # 指定字体路径
            stopwords=self.stopwords,
            max_words=200  # 显示的最大词数
        )

        # 生成词云
        wc.generate(string)
        wc.to_file(f'./data/{self.movie_name}/wordcloud.png')  # 保存词云图片

        # 使用matplotlib显示词云图
        plt.figure(figsize=(10, 8))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')  # 不显示坐标轴
        plt.show()
        