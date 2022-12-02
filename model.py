import pandas as pd
import numpy as np
import sklearn

df = pd.read_csv('diabetes.csv')
#print(df.shape)
X = df.iloc[:,:-1]
y = df.iloc[:,-1]

#print(X.head())
#print(y.head())
#Train-Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=0)

#Implement Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(X_train,y_train)

#Prediction
y_pred = classifier.predict(X_test)

#Check Accuracy
from sklearn.metrics import accuracy_score
score = accuracy_score(y_test,y_pred)
#print(score)

filename='diabetes_model.sav'
pickle.dump(clf,open(filename','wb')
