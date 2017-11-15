# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-10-11
    
"""
import numpy as np
from matplotlib import pylab


from sklearn import cross_validation
from sklearn.cluster import KMeans
from sklearn.cross_validation import cross_val_score
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix, classification_report, mean_squared_error
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import completeness_score, homogeneity_score

# CSV文件很容易被numpy类库的genfromtxt方法解析
# 创建了一个包含特征值的矩阵以及一个包含样本类型的向量
# 读取前四行
data = np.genfromtxt('numpy_cvs.csv', delimiter=',',usecols=(0, 1, 2, 3))
# 读取第五行
target = np.genfromtxt('numpy_cvs.csv', delimiter=',', usecols=(4), dtype=str)
# 可以通过查看我们加载的数据结构的shape值来确认数据集的大小
# print data.shape
# print target.shape
# 查看我们有多少种样本类型以及它们的名字
# print set(target)


# 使用pylab类库（matplotlib的接口）的plotting方法可以建一个二维散点图让我们在两个维度上分析数据集的两个特征值
# 使用第一和第三维度（花萼的长和宽）
# pylab.plot(data[target == 'setosa', 0], data[target == 'setosa', 2], 'bo')
# pylab.plot(data[target == 'versicolor', 0], data[target == 'versicolor', 2], 'ro')
# pylab.plot(data[target == 'virginica', 0], data[target == 'virginica', 2], 'go')
# # 图中有150个点，不同的颜色代表不同的类型；蓝色点代表山鸢尾，红色点代表变色鸢尾，绿色点代表维吉尼亚鸢尾。
# pylab.show()

# 绘制直方图
# 绘制数据中每一类型的第一个特性（花萼的长度）
# xmin = min(data[:, 0])
# xmax = max(data[:, 0])
# pylab.figure()
# pylab.subplot(411)
# pylab.hist(data[target == 'setosa', 0], color='b', alpha=0.7)
# pylab.xlim(xmin, xmax)
# pylab.subplot(412)
# pylab.hist(data[target == 'versicolor', 0], color='r', alpha=0.7)
# pylab.xlim(xmin, xmax)
# pylab.subplot(413)
# pylab.hist(data[target == 'virginica', 0], color='g', alpha=0.7)
# pylab.xlim(xmin, xmax)
# pylab.subplot(414)
# pylab.hist(data[:, 0], color='y', alpha=0.7)
# pylab.xlim(xmin, xmax)
# pylab.show()

# 用高斯朴素贝叶斯来分析
t = np.zeros(len(target))
t[target == 'setosa'] = 1
t[target == 'versicolor'] = 2
t[target == 'virginica'] = 3

# 分类

# 实例化和训练分类器
# classifier = GaussianNB()
# classifier.fit(data, t)

# print classifier.predict(data[0])
# print t[0]
# 使用训练集的数据来训练分类器，并使用测试集的数据来测试分类器。train_test_split方法正是实现此功能的
# 数据集被分一分为二，测试集被指定为源数据的40%（命名为test_size），我们用它反复训练我们的分类器并输出精确度
# train, test, t_train, t_test = cross_validation.train_test_split(data, t, test_size=0.4, random_state=0)
# classifier.fit(train,t_train) # train
# 一个分类器的精确度是通过正确分类样本的数量除以总样本的数量得出的。也就是说，它意味着我们正确预测的比例
# print classifier.score(test,t_test)

# 混淆矩阵,每列代表一个预测类的实例，每行代表一个实际类的实例。使用它可以很容易的计算和打印矩阵
# print confusion_matrix(classifier.predict(test),t_test)
# print classification_report(classifier.predict(test), t_test, target_names=['setosa', 'versicolor', 'virginica'])
# scores = cross_val_score(classifier, data, t, cv=6)
# print scores
# print np.mean(scores)


# 聚类
#
# kmeans = KMeans(3, init='random') # initialization
# kmeans.fit(data) # actual execution
# c = kmeans.predict(data)
# # print completeness_score(t, c)
# # print homogeneity_score(t, c)
# pylab.figure()
# pylab.subplot(211) # top figure with the real classes
# pylab.plot(data[t == 1, 0], data[t == 1, 2], 'bo')
# pylab.plot(data[t == 2, 0], data[t == 2, 2], 'ro')
# pylab.plot(data[t == 3, 0], data[t == 3, 2], 'go')
# pylab.subplot(212) # bottom figure with classes assigned automatically
# pylab.plot(data[c == 1, 0],data[c == 1, 2], 'bo', alpha=.7)
# pylab.plot(data[c == 2, 0],data[c == 2, 2], 'go', alpha=.7)
# pylab.plot(data[c == 0, 0],data[c == 0, 2], 'mo', alpha=.7)
# pylab.show()


# 回归
# 线性回归
# x = np.random.rand(40, 1)
# y = x * x * x + np.random.rand(40, 1)/5
# # LinearRegression模型。该模型可以通过计算每个数据点到拟合线的垂直差的平方和，找到平方和最小的最佳拟合线
# linreg = LinearRegression()
# linreg.fit(x, y)
# # 把拟合线和实际数据点画在同一幅图上来评估结果
# xx = np.linspace(0, 1, 40)
# pylab.plot(x, y, 'o', xx, linreg.predict(np.matrix(xx).T), '--r')
# pylab.show()
# # 使用均方误差来量化模型和原始数据的拟合度
# print mean_squared_error(linreg.predict(x),y)


# 相关
# 皮尔逊积矩相关系数。它是由两个变量的协方差除以它们的标准差的乘积计算而来。我们将鸢尾花数据集的变量两两组合计算出其系数如下所示
# corr = np.corrcoef(data.T)
# print corr
# # corrcoef方法通过输入行为变量列为观察值的矩阵，计算返回相关系数的对称矩阵。该矩阵的每个元素代表着两个变量的相关性。
# pylab.pcolor(corr)
# pylab.colorbar()  # add
# # arranging the names of the variables on the axis
# pylab.xticks(np.arange(0.5, 4.5), ['sepal length',  'sepal width', 'petal length', 'petal width'], rotation=-20)
# pylab.yticks(np.arange(0.5, 4.5), ['sepal length',  'sepal width', 'petal length', 'petal width'], rotation=-20)
# pylab.show()


# 降维
# 降维技术之一就是主成分分析（PCA）。该技术把数据变量转换为等量或更少的不相关变量，称为主成分（PCs）。
# pca = PCA(n_components=2)
# pcad = pca.fit_transform(data)
# pylab.plot(pcad[target=='setosa', 0], pcad[target=='setosa', 1], 'bo')
# pylab.plot(pcad[target=='versicolor', 0], pcad[target=='versicolor', 1], 'ro')
# pylab.plot(pcad[target=='virginica', 0], pcad[target=='virginica', 1], 'go')
# pylab.show()
#通过方差比判断PCs包含的信息量
# print pca.explained_variance_ratio_
# print 1-sum(pca.explained_variance_ratio_)


# 网络挖掘










