#import necessary libraries
import pandas as pd
import joblib

#loading the saved model
load_model=joblib.load("Project_Saved_Models/pipeline_knn_model_99acc.sav")

info=[]
parameters=['fruit_label','ppm']

fruit_label=input("enter fruit label (eg:apple-1,orange-2) :")
info.append(fruit_label)
ppm=input("enter formaldehyde content (in ppm)  :")
info.append(ppm)

my_dict=dict(zip(parameters,info))

#convert dict into dataframe
my_data=pd.DataFrame(my_dict,index=[0])

# dataframe is putting into the MODEL to make PREDICTION
my_pred = load_model.predict(my_data)
print(my_pred)
my_pred = my_pred[0]
print(my_pred)

print("Result:")
if my_pred==0:
	print("UNSAFE")
if my_pred==1:
	print("SAFE")
