import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import joblib

data=pd.read_csv("employee_salary_150.csv")
data=data.dropna()
print(data.to_string())
data["Experience_Months"]=data["Experience_Years"]*12
x=data[["Experience_Months","Education_Level","Skill_Score","Age"]]
y=data["Salary_LKR"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=40)
regressor=LinearRegression()
regressor.fit(x_train,y_train)
print(pd.DataFrame(regressor.coef_,x.columns,columns=["Coefficient"]))
y_pred=regressor.predict(x_test)
print("R2 Score:",round(r2_score(y_test,y_pred),2))
print("Mean Squared Error:",round(mean_squared_error(y_test,y_pred),2))

joblib.dump(regressor,"employee_salary_150.pkl")
print("Model saved Successfully")
