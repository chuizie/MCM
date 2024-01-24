# 导入必要的库
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import datasets

# 加载示例数据集（这里以Iris数据集为例）
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 将数据集拆分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建Logistic回归模型
model = LogisticRegression()

# 训练模型
model.fit(X_train, y_train)

# 在测试集上进行预测
predictions = model.predict(X_test)

# 打印预测结果
print("预测结果:", predictions)

# 打印模型准确率
accuracy = model.score(X_test, y_test)
print("模型准确率:", accuracy)
