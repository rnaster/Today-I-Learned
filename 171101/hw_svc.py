import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
train = pd.read_csv('train.csv')
cv = pd.read_csv('valid.csv')
train_X, train_y = train.drop('Class', axis=1), train.Class
cv_X, cv_y = cv.drop('Class', axis=1), cv.Class
f1 = lambda x, y: 2 * x * y / (x + y) if x != 0 and y != 0 else 0

idx = 1
result_svc = pd.DataFrame(columns=['C', 'Gamma', 'recall', 'precision', 'F1_score', 'mtx1', 'mtx2', 'mtx3', 'mtx4'])
C = 0.9
while C <= 1:
	gamma = 0.0001
	while gamma < 1:
		svc = SVC(decision_function_shape='ovo', class_weight='balanced', C=C, gamma=gamma, random_state=18)
		svc.fit(train_X, train_y)
		svc_pred = svc.predict(cv_X)
		mtx = confusion_matrix(cv_y, svc_pred)
		prec = mtx[1,1] / sum(mtx[:,1]) if sum(mtx[:,1]) else 0
		rec = mtx[1,1] / sum(mtx[1, :])
		result_svc.loc[idx] = [C, gamma, rec, prec, f1(rec, prec), *mtx.flatten()]
		print(idx, 'svc')
		print(result_svc.loc[idx])
		idx += 1
		gamma += 0.0001
		if idx % 10 ==0: result_svc.to_csv('result_svc.csv')
	C += 0.0001
result_svc.to_csv('result_svc.csv')