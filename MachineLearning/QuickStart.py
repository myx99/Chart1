from sklearn import datasets
from sklearn import svm


iris = datasets.load_iris()
digits = datasets.load_digits()
# print(digits.target)

clf = svm.SVC(gamma=0.001, c=100.)