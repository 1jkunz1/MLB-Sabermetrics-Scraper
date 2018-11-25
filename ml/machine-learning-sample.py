import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

'''https://medium.freecodecamp.org/the-hitchhikers-guide-to-machine-learning-algorithms-in-python-bfad66adb378'''


class MachineLearningExamples(object):

	def __init__(self):
		pass

	def linear_regression(self):

		"""
		Linear Regression

		Perhaps the most popular machine learning algorithm out there and definitely the most under appreciated.
		Many data scientists have a tendency to forget that simpler is almost always preferred over complex when performance
		is comparable.

		Anyways, linear regression is a supervised learning algorithm that predicts an outcome based on continuous features.
		Linear regression is versatile in the sense that it has the ability to be run on a single variable (simple linear
		regression) or on many features (multiple linear regression). The way it works is by assigning optimal weights to the
		variables in order to create a line (ax + b) that will be used to predict output.
		"""

		from sklearn import linear_model
		df = pd.read_csv('linear_regression_df.csv')
		df.columns = ['X', 'Y']
		df.head()

		sns.set_context("notebook", font_scale=1.1)
		sns.set_style("ticks")
		sns.lmplot('X', 'Y', data=df)
		plt.ylabel('Response')
		plt.xlabel('Explanatory')

		linear = linear_model.LinearRegression()
		trainX = np.asarray(df.X[20:len(df.X)]).reshape(-1, 1)
		trainY = np.asarray(df.Y[20:len(df.Y)]).reshape(-1, 1)
		testX = np.asarray(df.X[:20]).reshape(-1, 1)
		testY = np.asarray(df.Y[:20]).reshape(-1, 1)
		linear.fit(trainX, trainY)
		linear.score(trainX, trainY)
		print('Coefficient: \n', linear.coef_)
		print('Intercept: \n', linear.intercept_)
		print('R² Value: \n', linear.score(trainX, trainY))
		predicted = linear.predict(testX)
		return predicted

	def logistic_regression(self):

		"""
		Logistic regression is a supervised classification algorithm and therefore is useful for estimating discrete values.
		It is typically used for predicting the probability of an event using the logistic function in order to get an output
		between 0 and 1.

		When first learning this logistic regression, I was under the impression that it was a sort of a niche thing and
		therefore I didn' give it my full attention. In hindsight, I couldn' have been more wrong.
		Some of the underlying aspects of logistic regression come up in many other important machine learning algorithms
		like neural networks. With this in mind, go ahead and check out the video below for more.
		"""

		from sklearn.linear_model import LogisticRegression
		df = pd.read_csv('logistic_regression_df.csv')
		df.columns = ['X', 'Y']
		df.head()

		sns.set_context("notebook", font_scale=1.1)
		sns.set_style("ticks")
		sns.regplot('X', 'Y', data=df, logistic=True)
		plt.ylabel('Probability')
		plt.xlabel('Explanatory')

		logistic = LogisticRegression()
		X = (np.asarray(df.X)).reshape(-1, 1)
		Y = (np.asarray(df.Y)).ravel()
		logistic.fit(X, Y)
		logistic.score(X, Y)
		print('Coefficient: \n', logistic.coef_)
		print('Intercept: \n', logistic.intercept_)
		print('R² Value: \n', logistic.score(X, Y))

	def decision_trees(self):

		"""Decision trees are a form of supervised learning that can be used for both classification and regression purposes.
		In my experience, they are typically utilized for classification purposes. The model takes in an instance and then
		goes down the tree, testing significant features against a determined conditional statement. Depending on the result,
		it will go down to the left or right child branch and onward after that. Typically the most significant features in
		the process will fall closer to the root of the tree.

		Decision trees are becoming increasingly popular and can serve as a strong learning algorithm for any data scientist to
		have in their repertoire, especially when coupled with techniques like random forests, boosting, and bagging.
		Once again, use the video below for a more in-depth look into the underlying functionality of decision trees."""
		from sklearn import tree
		df = pd.read_csv('iris_df.csv')
		df.columns = ['X1', 'X2', 'X3', 'X4', 'Y']
		df.head()

		from sklearn.model_selection import train_test_split
		decision = tree.DecisionTreeClassifier(criterion='gini')
		X = df.values[:, 0:4]
		Y = df.values[:, 4]
		trainX, testX, trainY, testY = train_test_split(X, Y, test_size=0.3)
		decision.fit(trainX, trainY)
		print('Accuracy: \n', decision.score(testX, testY))

		from sklearn.externals.six import StringIO
		from IPython.display import Image
		import pydotplus as pydot
		dot_data = StringIO()
		tree.export_graphviz(decision, out_file=dot_data)
		graph = pydot.graph_from_dot_data(dot_data.getvalue())
		Image(graph.create_png())
