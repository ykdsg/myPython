import os
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

# 加载停用词
with open('./text/stop/stopword.txt', 'rb') as f:
    stop_words = [line.strip() for line in f.readlines()]


def cut_words(file_path):
    """
    对文本进行切词
    :param file_path:txt文本路径
    :return:用空格分词的字符串
    """
    text_with_spaces = ''
    text = open(file_path, 'r', encoding='gb18030').read()
    textcut = jieba.cut(text)
    for word in textcut:
        text_with_spaces += word + ' '
    return text_with_spaces


def loadfile(file_dir):
    """
    将路径下的所有文件加载
    :param file_dir:文件目录
    :return:分词后的文档列表和标签
    """
    words_list = []
    labels_list = []

    file_list = os.listdir(file_dir)
    for label_file in file_list:
        label_file_path = file_dir + '/' + label_file
        for file in os.listdir(label_file_path):
            file_path = label_file_path + '/' + file
            words_list.append(cut_words(file_path))
            labels_list.append(label_file)

    # for file in file_list:
    #     file_path = file_dir + '/' + file
    #     words_list.append(cut_words(file_path))
    #     labels_list.append(label)

    return words_list, labels_list


# 训练数据
# train_words1, train_labels1 = loadfile('./text/train/女性', '女性')
# train_words2, train_labels2 = loadfile('./text/train/体育', '体育')
# train_words3, train_labels3 = loadfile('./text/train/文学', '文学')
# train_words4, train_labels4 = loadfile('./text/train/校园', '校园')
#
# train_words = train_words1 + train_words2 + train_words3 + train_words4
# train_labels = train_labels1 + train_labels2 + train_labels3 + train_labels4

train_words, train_labels = loadfile('./text/train')
test_words, test_labels = loadfile('./text/test')

# 计算单词权重
#  max_df 参数用来描述单词在文档中的最高出现率。假设 max_df=0.5，代表一个单词在 50% 的文档中都出现过了，那么它只携带了非常少的信息，因此就不作为分词统计。
tf = TfidfVectorizer(stop_words=stop_words, max_df=0.5)
# 使用 fit_transform 方法进行拟合，得到 TF-IDF 特征空间 features，你可以理解为选出来的分词就是特征。我们计算这些特征在文档上的特征向量，得到特征空间 features。
train_features = tf.fit_transform(train_words)
# 上面fit过了，这里用transform()函数把测试集特征维度转成与训练集特征维度相同
test_features = tf.transform(test_words)
# 当 alpha=1 时，使用的是 Laplace 平滑。Laplace 平滑就是采用加 1 的方式，来统计没有出现过的单词的概率。这样当训练样本很大的时候，加 1 得到的概率变化可以忽略不计，也同时避免了零概率的问题
# 当 0<alpha<1 时，使用的是 Lidstone 平滑。对于 Lidstone 平滑来说，alpha 越小，迭代次数越多，精度越高。我们可以设置 alpha 为 0.001。
clf = MultinomialNB(alpha=0.001).fit(train_features, train_labels)
# 用训练好的分类器对新数据做预测
# 传入测试集的特征矩阵 test_features，得到分类结果 predicted_labels。predict 函数做的工作就是求解所有后验概率并找出最大的那个。
predicted_labels = clf.predict(test_features)
# 计算准确率
print('准确率为：', metrics.accuracy_score(test_labels, predicted_labels))
