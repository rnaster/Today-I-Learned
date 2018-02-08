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

'''
idx = 1
result_svc = pd.DataFrame(columns=['C', 'Gamma', 'recall', 'precision', 'F1_score', 'mtx1', 'mtx2', 'mtx3', 'mtx4'])
C = 0.9
while C:
	gamma = 0.00001
	while gamma:
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
		gamma -= 0.000005
		if idx % 10 ==0: result_svc.to_csv('result_svc.csv')
	C -= 0.05
'''

idx = 1
result_mlp = pd.DataFrame(columns=['h1','h2','h3','h4','h5','h6',
				'recall', 'precision', 'F1_score', 'mtx1', 'mtx2', 'mtx3', 'mtx4'])
for h1 in range(200, 300):
	for h2 in range(200, 300):
		for h3 in range(200, 300):
			for h4 in range(200, 300):
				for h5 in range(200, 300):
					for h6 in range(200, 300):
						mlp = MLPClassifier(hidden_layer_sizes=(h1, h2, h3, h4, h5, h6),
						                    activation='relu', solver='adam', validation_fraction=0, alpha=0.00001, random_state=18)
						mlp.fit(train_X, train_y)
						cv_pred = mlp.predict(cv_X)
						mtx = confusion_matrix(cv_y, cv_pred)
						prec = mtx[1,1] / sum(mtx[:,1]) if sum(mtx[:,1]) else 0
						rec = mtx[1,1] / sum(mtx[1, :])
						result_mlp.loc[idx] = [h1, h2, h3, h4, h5, h6, rec, prec, f1(prec, rec), *mtx.flatten()]
						print(idx,'mlp')
						print(result_mlp.loc[idx])
						if idx % 200 == 0: result_mlp.to_csv('result_mlp.csv')
						idx += 1
result_mlp.to_csv('result_mlp.csv')