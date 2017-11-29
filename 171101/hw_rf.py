import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier

train = pd.read_csv('train.csv')
cv = pd.read_csv('valid.csv')
train_X, train_y = train.drop('Class', axis=1), train.Class
cv_X, cv_y = cv.drop('Class', axis=1), cv.Class
f1 = lambda x, y: 2 * x * y / (x + y) if x != 0 and y != 0 else 0

idx = 1
result_RF = pd.DataFrame(columns=['', 'recall', 'precision', 'F1_score', 'mtx1', 'mtx2', 'mtx3', 'mtx4'])

rf = RandomForestClassifier(criterion='entropy', max_features='sqrt', n_estimators=2000,
 		random_state=18, class_weight='balanced', )
rf.fit(train_X, train_y)
# rf_pred = rf.predict(cv_X)
# mtx = confusion_matrix(cv_y, rf_pred)
# prec = mtx[1,1] / sum(mtx[:,1]) if sum(mtx[:,1]) else 0
# rec = mtx[1,1] / sum(mtx[1, :])
# print(prec, rec, f1(prec, rec), '\n', mtx)

def rf_predict(file):
	test = pd.read_csv(file)
	return rf.predict(test)
