#import necessary libraries
import pandas as pd

from sklearn.model_selection import train_test_split

from imblearn.over_sampling import SMOTE
from collections import Counter

from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

import joblib


#load dataset
data=pd.read_excel("Project_Dataset/dataset.xlsx")
print(data.head())
print(data.columns)

#####Preprocessing
#converting categorical values to numerical
data['fruit_label']=data['fruit_label'].replace("apple",1)
data['fruit_label']=data['fruit_label'].replace("orange",2)
data['state']=data['state'].replace("unsafe",0)
data['state']=data['state'].replace("safe",1)

print(data.head())

# saving the preprocessed dataset
# data.to_excel("Project_Dataset/preprocessed_dataset.xlsx",index=False)

#load preprocessed dataset
my_data=pd.read_excel("Project_Dataset/preprocessed_dataset.xlsx")
print(my_data.head())

#data division (independent variable & dependent variable)
y=my_data['state']
x=my_data.drop(['state'],axis=1)

print(x)
print(y)

######Train-Test Splitting
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

#Data balancing using SMOTE
counter = Counter(y_train)
print("__________________BEFORE::::::", counter)

smt = SMOTE()

x_train_sm, y_train_sm = smt.fit_resample(x_train, y_train)

counter = Counter(y_train_sm)
print("___________________AFTER:::::::", counter)


print("x_train_sm shape:", x_train_sm.shape)
print("y_train_sm shape:", y_train_sm.shape)











#Model creation-Pipline(standardization & SVM)
scaler=StandardScaler()

#svm model loading
svm=SVC()
pipe_svm=Pipeline([('scaler',StandardScaler()),('svm',SVC())])
#training
pipe_svm.fit(x_train_sm,y_train_sm)
prediction=pipe_svm.predict(x_test)

# calculate accuracy =(TP+TN)/total
acc = accuracy_score(y_test, prediction)
print(f"The accuracy score for SVM is :{round(acc,3)*100}%")

# model saving
filename = "Project_Saved_Models/pipeline_svm_model.sav"
joblib.dump(pipe_svm, filename)






#knn classifier model loading
knn=KNeighborsClassifier()
pipe_knn=Pipeline([('scaler',StandardScaler()),('knn',KNeighborsClassifier())])
#training
pipe_knn.fit(x_train_sm,y_train_sm)
prediction=pipe_knn.predict(x_test)

# calculate accuracy =(TP+TN)/total
acc = accuracy_score(y_test, prediction)
print(f"The accuracy score for KNN is :{round(acc,3)*100}%")

# model saving
filename = "Project_Saved_Models/pipeline_knn_model.sav"
joblib.dump(pipe_knn, filename)






